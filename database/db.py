from pymongo import MongoClient
from werkzeug.security import generate_password_hash

MONGO_URI = "mongodb://admin:12345@127.0.0.1:27017/?authSource=admin"
client = MongoClient(MONGO_URI)

db = client["Agri_db"]

users_collection = db["users"]
predictions_collection = db["predictions"]
blogs_collection = db["blogs"]
quizzes_collection = db["quizzes"]
contact_collection = db["contact_messages"]

def insert_contact_message(data):
    contact_collection.insert_one(data)

#  RUN THIS ONLY ONCE TO CREATE ADMIN
def create_admin_user():
    admin = users_collection.find_one({"username": "admin"})
    hashed_pw = generate_password_hash("admin123")
    if not admin:
        users_collection.insert_one({
            "username": "admin",
            "email": "admin@agrismart.com",
            "password": hashed_pw,
            "role": "admin"
        })
        print(" Admin user created.")
    else:
        users_collection.update_one(
            {"username": "admin"},
            {"$set": {
                "password": hashed_pw,
                "role": "admin"
            }}
        )
        print(" Admin password & role updated.")

