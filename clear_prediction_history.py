from pymongo import MongoClient

client = MongoClient("mongodb://admin:12345@127.0.0.1:27017/?authSource=admin")

db = client["Agri_db"]
predictions_collection = db["predictions"]

# Delete all documents in the 'predictions' collection
result = predictions_collection.delete_many({})

print(f" Deleted {result.deleted_count} prediction history records.")


