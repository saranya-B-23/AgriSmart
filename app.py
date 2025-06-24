from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
import pickle
import random
from datetime import datetime
from database.db import db, users_collection, predictions_collection, blogs_collection
from utils.weather import get_weather_data
from database.db import quizzes_collection
from utils.gamify import update_xp
from flask import flash
from database.db import insert_contact_message, contact_collection
from utils.chatbot import get_answer,load_chatbot_data
import os
import tensorflow as tf
import numpy as np
from PIL import Image
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = "your_secret_key"

# Load ML Model
with open("model/model1.pkl", "rb") as f:
    model = pickle.load(f)

# Load your soil model
soil_model = tf.keras.models.load_model('soil_model.h5')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users_collection.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            session["username"] = username
            session["role"] = user.get("role", "user")
            return redirect(url_for("predict"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Check for existing user
        if users_collection.find_one({"username": username}):
            return render_template("register.html", error="Username already exists")

        # Optional fields
        age = request.form.get("age")
        gender = request.form.get("gender")
        experience = request.form.get("experience")
        crops = request.form.get("crops")
        contact_method = request.form.get("contact_method")
        smartphone = request.form.get("smartphone")

        # Store the user
        hashed_pw = generate_password_hash(password)
        user_data = {
            "username": username,
            "email": email,
            "password": hashed_pw,
            "age": int(age) if age else None,
            "gender": gender,
            "experience": int(experience) if experience else None,
            "crops": [crop.strip() for crop in crops.split(",")] if crops else [],
            "contact_method": contact_method,
            "smartphone": smartphone,
        }

        users_collection.insert_one(user_data)
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        try:
            city = request.form.get("city", "Unknown")
            soil_type = request.form.get("soil_type", "Unknown")

            N = float(request.form.get("N", 0))
            P = float(request.form.get("P", 0))
            K = float(request.form.get("K", 0))
            temperature = float(request.form.get("temperature", 0))
            humidity = float(request.form.get("humidity", 0))
            pH = float(request.form.get("ph", 0))
            rainfall = float(request.form.get("rainfall", 0))

            if not all([N, P, K, temperature, humidity, pH, rainfall]):
                raise ValueError("Incomplete form values")

            features = [N, P, K, temperature, humidity, pH, rainfall]
            prediction = model.predict([features])[0]

            parts = prediction.split(",")
            crop = parts[0].strip()
            water = parts[1].strip()
            fertilizer = parts[2].strip()
            pesticide = ",".join(parts[3:]).strip()
            combined_fp = f" {fertilizer}  {pesticide}"

            prediction_doc = {
                "username": session["username"],
                "city": city,
                "N": N,
                "P": P,
                "K": K,
                "temperature": temperature,
                "humidity": humidity,
                "ph": pH,
                "rainfall": rainfall,
                "crop": crop,
                "water": water,
                "fertilizer": fertilizer,
                "pesticide": pesticide,
                "fertilizer_pesticide": combined_fp,
                "timestamp": datetime.now()
            }
            predictions_collection.insert_one(prediction_doc)

            session['last_prediction'] = {
                "label": crop,
                "Water_Requirement": water,
                "Fertilizer": fertilizer,
                "Pesticide": pesticide,
                "Combined": combined_fp,
                "temperature": temperature,
                "humidity": humidity,
                "rainfall": rainfall,
                "city": city,
                "N": N,
                "P": P,
                "K": K,
                "pH": pH,
                "soil_type": soil_type
            }

            return redirect(url_for("predict_result"))

        except Exception as e:
            print("Prediction error:", e)
            return render_template("predict.html", error="Please enter valid input values.")

    return render_template("predict.html")

@app.route("/predict_result")
def predict_result():
    if "username" not in session:
        return redirect(url_for("login"))

    prediction = session.pop('last_prediction', None)
    if not prediction:
        return redirect(url_for("predict"))

    return render_template("predict_result.html", prediction=prediction)


@app.route("/get_weather")
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City not provided"}), 400

    weather = get_weather_data(city)

    if None in weather.values():
        return jsonify({"error": "Failed to fetch weather data"}), 500

    temperature = round(weather["temperature"], 1)
    humidity = round(weather["humidity"], 1)
    rainfall = round(weather["rainfall"], 1)

    if rainfall == 0.0:
        rainfall = round(random.uniform(20, 100), 1)

    return jsonify({
        "temperature": temperature,
        "humidity": humidity,
        "rainfall": rainfall
    })

@app.route("/prediction_history")
def prediction_history():
    if "username" not in session:
        return redirect(url_for("login"))


    raw_records = predictions_collection.find({
        "username": session["username"],
        "crop": {"$ne": None},
        "fertilizer": {"$ne": None},
        "pesticide": {"$ne": None},
        "water": {"$ne": None}
    }).sort("timestamp", -1)

    predictions = []
    for rec in raw_records:
        predictions.append({
            "timestamp": rec.get("timestamp"),
            "inputs": {
                "city": rec.get("city", "Unknown"),
                "N": rec.get("N"),
                "P": rec.get("P"),
                "K": rec.get("K"),
                "temperature": rec.get("temperature"),
                "humidity": rec.get("humidity"),
                "ph": rec.get("ph"),
                "rainfall": rec.get("rainfall"),
            },
            "result": {
                "crop": rec.get("crop"),
                "fertilizer": rec.get("fertilizer"),
                "pesticide": rec.get("pesticide"),
                "water": rec.get("water"),
                "combined": rec.get("fertilizer_pesticide")
            }
        })
    return render_template("prediction_history.html", predictions=predictions)


@app.route("/blog", methods=["GET", "POST"])
def blog():
    if "username" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        blogs_collection.insert_one({
            "author": session["username"],
            "title": title,
            "content": content,
            "timestamp": datetime.now()
        })
    all_blogs = blogs_collection.find().sort("timestamp", -1)
    return render_template("blog.html", blogs=all_blogs)

@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
    return render_template('blog_detail.html', blog=blog)

@app.route('/blog/<blog_id>/like', methods=['POST'])
def like_blog(blog_id):
    blogs_collection.update_one(
        {"_id": ObjectId(blog_id)},
        {"$inc": {"likes": 1}}
    )
    return redirect(url_for('blog_detail', blog_id=blog_id))

@app.route('/blog/<blog_id>/comment', methods=['POST'])
def add_comment(blog_id):
    comment_text = request.form['comment']
    comment = {
        "user": session.get("username", "Anonymous"),
        "comment": comment_text,
        "timestamp": datetime.utcnow()
    }
    blogs_collection.update_one(
        {"_id": ObjectId(blog_id)},
        {"$push": {"comments": comment}}
    )
    return redirect(url_for('blog_detail', blog_id=blog_id))

# Load the chatbot data
chatbot_df = load_chatbot_data()

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_msg = request.form.get('message', '').strip()
        if not user_msg:
            return jsonify({'response': " Please enter a message."})
        answer = get_answer(user_msg, chatbot_df)
        return jsonify({'response': answer})
    return render_template('chatbot.html')


@app.route("/gamification")
def gamification():
    if "username" not in session:
        return redirect(url_for("login"))
    if "quiz_progress" not in session:
        session["quiz_progress"] = 1
    return render_template("gamification.html")

@app.route("/quiz/<int:level>", methods=["GET"])
def quiz(level):
    if "username" not in session:
        return redirect(url_for("login"))

    session["quiz_start_time"] = datetime.utcnow().isoformat()
    session["quiz_level"] = level

    quiz_data = quizzes_collection.find_one({"level": level})
    if not quiz_data:
        return "Quiz not found", 404

    return render_template(
        "quiz.html",
        level=level,
        questions=quiz_data["questions"],
        quiz_start_time=session["quiz_start_time"]
    )

@app.route("/quiz/<int:level>/submit", methods=["POST"])
def submit_quiz(level):
    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]
    quiz_data = quizzes_collection.find_one({"level": level})
    if not quiz_data:
        return "Quiz not found", 404

    questions = quiz_data["questions"]
    score = 0
    attempted = False  #  track if user selected any option

    for idx, q in enumerate(questions):
        user_answer = request.form.get(f"q{idx}")
        if user_answer:  # answered anything?
            attempted = True
            if user_answer == q["answer"]:
                score += 1

    if not attempted:

        from flask import flash
        flash(" You must answer at least one question!", "danger")
        return redirect(url_for("quiz", level=level))

    xp_earned = score * 15
    new_level, new_badges = update_xp(username, xp_earned, level)

    next_level = level + 1
    if session.get("quiz_progress", 1) < next_level:
        session["quiz_progress"] = next_level

    session.pop("quiz_start_time", None)
    session.pop("quiz_level", None)

    return render_template(
        "result.html",
        level=level,
        score=score,
        xp_earned=xp_earned,
        new_level=new_level,
        new_badges=new_badges,
        next_level=next_level
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")

@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not name or not email or not message:
        flash("All fields are required.", "danger")
        return redirect(url_for("contact"))

    contact_data = {
        "name": name,
        "email": email,
        "message": message,
        "submitted_at": datetime.utcnow()
    }

    insert_contact_message(contact_data)
    flash("Thank you! Your message has been submitted.", "success")
    return redirect(url_for("contact"))

@app.route("/admin/contact-messages")
def view_contact_messages():
    if session.get("role") != "admin":
        return redirect(url_for("home"))

    messages = list(contact_collection.find().sort("submitted_at", -1))
    return render_template("admin_contact_messages.html", messages=messages)

@app.route("/crop_calendar")
def crop_calendar():
    return render_template("crop_calendar.html")

@app.route("/tips_guides")
def tips_guides():
    return render_template("tips_Guides.html")

@app.route("/user_guidelines")
def user_guidelines():
    return render_template("user_guidelines.html")

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = session['username']

    predictions = list(predictions_collection.find({'username': user}))

    total_predictions = len(predictions)

    from collections import Counter
    crop_counter = Counter([p.get("crop") for p in predictions if p.get("crop")])
    most_common_crop = crop_counter.most_common(1)[0][0] if crop_counter else None

    def safe_avg(key):
        vals = [p.get(key) for p in predictions if p.get(key) is not None]
        return round(sum(vals)/len(vals), 2) if vals else None

    avg_n = safe_avg("N")
    avg_p = safe_avg("P")
    avg_k = safe_avg("K")

    return render_template(
        "dashboard.html",
        most_common_crop=most_common_crop,
        avg_n=avg_n,
        avg_p=avg_p,
        avg_k=avg_k,
        total_predictions=total_predictions,
        predictions=predictions
    )
soil_parameter_ranges = {
    "Alluvial soil": {
        "N": (40, 80),
        "P": (20, 40),
        "K": (15, 35),
        "pH": (6.0, 7.5)
    },
    "Black soil": {
        "N": (30, 60),
        "P": (10, 25),
        "K": (30, 60),
        "pH": (7.5, 8.5)
    },
    "Clay soil": {
        "N": (20, 50),
        "P": (10, 30),
        "K": (10, 30),
        "pH": (6.0, 7.0)
    },
    "Red soil": {
        "N": (10, 40),
        "P": (5, 15),
        "K": (5, 20),
        "pH": (5.5, 6.5)
    }
}

soil_labels = list(soil_parameter_ranges.keys())

@app.route('/detect_soil', methods=['POST'])
def detect_soil():
    if 'soil_image' not in request.files:
        return jsonify({"success": False, "message": "No image uploaded."})

    image_file = request.files['soil_image']

    try:

        filename = secure_filename(image_file.filename)
        upload_path = os.path.join("static/uploads", filename)
        os.makedirs(os.path.dirname(upload_path), exist_ok=True)
        image_file.save(upload_path)

        # Preprocess
        image = Image.open(upload_path).convert('RGB')
        image = image.resize((224, 224))
        img_array = np.array(image) / 255.0
        img_array = img_array.reshape((1, 224, 224, 3))

        prediction = soil_model.predict(img_array)
        predicted_index = np.argmax(prediction)
        soil_type = soil_labels[predicted_index]

        ranges = soil_parameter_ranges.get(soil_type)
        values = {
            "N": random.randint(*ranges["N"]),
            "P": random.randint(*ranges["P"]),
            "K": random.randint(*ranges["K"]),
            "pH": round(random.uniform(*ranges["pH"]), 1)
        }


        prediction_record = {
            "username": session.get("username", "guest"),
            "prediction_type": "soil",
            "soil_type": soil_type,
            "N": values["N"],
            "P": values["P"],
            "K": values["K"],
            "pH": values["pH"],
            "image_filename": filename,
            "timestamp": datetime.now()
        }
        predictions_collection.insert_one(prediction_record)

        return jsonify({
            "success": True,
            "soil_type": soil_type,
            **values
        })

    except Exception as e:
        print("Soil detection error:", e)
        return jsonify({"success": False, "message": "Error processing image."})

if __name__ == "__main__":
    app.run(debug=True)