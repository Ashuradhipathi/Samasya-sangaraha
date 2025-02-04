import os
from pymongo.mongo_client import MongoClient

# Initialize client
client = MongoClient(os.getenv("uri"), serverSelectionTimeoutMS=60000)

# Initialize db, collection
database = client["Samasya-sangraha"]
collection = database["sangraha"]


# function to retrieve all problems from db
def retrieve_all():
    records = collection.find({})
    print("Records fetching")
    return list(records)
