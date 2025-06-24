# AgriSmart 🌾

AgriSmart is a final-year engineering project that uses machine learning to recommend suitable crops and relevant fertilizers, pesticides, and water needs based on real-time environmental conditions and soil data.

---

##  Key Features

-  **Crop Prediction** using ML (`model/model1.pkl`)
-  **Auto-filled Weather Parameters** using OpenWeather API (via city name)
-  **Fertilizer, Pesticide, Water Suggestions** for the predicted crop
-  **Soil Parameter Detection** from uploaded image (`soil_model.h5`)
-  **Local Chatbot** trained on 1000+ Q&A from `data/farmer_chatbot_qa.csv`
-  Extra Modules: Agri Tips, Crop Calendar, Blogs, Quiz, FAQ, Contact

---

## 📁 Folder Structure

```
AgriSmart/
├── app.py
├── main.py
├── model/
│   └── model1.pkl
├── soil_model.h5
├── train_soil_model.py
├── test_soil_model.py
├── database/
│   ├── db.py
│   ├── seed_blogs.py
│   └── seed_quiz_levels.py
├── dataset/
│   ├── data_collection.py
│   ├── data_preprocessing.py
├── static/
│   ├── style.css
│   └── images/, uploads/
├── templates/
│   ├── layout.html, predict.html, result.html, etc.
├── utils/
│   ├── chatbot.py
│   ├── weather.py
│   └── gamify.py
├── data/
│   ├── crop.csv
│   ├── farmer_chatbot_qa.csv
├── soil_dataset/        
```

---

## 📦 Dataset Download

All required datasets and trained models are available at the Dropbox link below:

🔗 [Download Datasets](https://www.dropbox.com/scl/fo/hjereeabufk60nl2embtl/AOyAM-HGy_FDrCUCAVIHBHk?rlkey=wxcdos66z08xskoj962hzv1vx&st=5vopc70e&dl=0)

This includes:
- `crop.csv`
- `farmer_chatbot_qa.csv`
- `soil_dataset.zip`

---

## ▶️ To Run the Project

```bash
pip install -r requirements.txt
python app.py
```

Then open: `http://127.0.0.1:5000/` in your browser.

---

🎓 **Final Year Project - Dept. of CSE, 2025**
