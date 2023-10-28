```python
import time
from functools import wraps
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ai_interview_db']
cache_db = db['cache']

# Define a decorator for caching
def cache(ttl=300):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate a unique key for this function and its arguments
            key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            # Check if data is in cache
            cached_result = cache_db.find_one({"_id": key})
            if cached_result:
                # If the data is not expired, return it
                if time.time() - cached_result['time'] < ttl:
                    return cached_result['result']
                # If the data is expired, delete it
                else:
                    cache_db.delete_one({"_id": key})
            # If the data was not in cache or was expired, run the function
            result = func(*args, **kwargs)
            # Save the result in cache
            cache_db.insert_one({"_id": key, "result": result, "time": time.time()})
            return result
        return wrapper
    return decorator
```