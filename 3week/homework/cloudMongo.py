from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://nam2350:park@2350@webtest-tspyf.mongodb.net/test?retryWrites=true&w=majority"
)

db = client["db"]
collection = db["collection"]
