```python
import pymongo
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['user_analytics']

# User Analytics Collection
user_analytics_collection = db['user_analytics']

def log_user_activity(user_id, activity):
    """
    Logs user activity into the MongoDB collection
    """
    user_activity = {
        "user_id": user_id,
        "activity": activity,
        "timestamp": datetime.now()
    }
    user_analytics_collection.insert_one(user_activity)

def get_user_activity(user_id):
    """
    Retrieves user activity from the MongoDB collection
    """
    user_activity = user_analytics_collection.find({"user_id": user_id})
    return list(user_activity)

def get_all_user_activity():
    """
    Retrieves all user activity from the MongoDB collection
    """
    all_user_activity = user_analytics_collection.find()
    return list(all_user_activity)
```