```python
from elasticsearch import Elasticsearch
from datetime import datetime
import logging

# Initialize Elasticsearch
es = Elasticsearch()

# Initialize logging
logging.basicConfig(level=logging.INFO)

def log_system_performance(systemPerformanceData):
    """
    Logs system performance data to Elasticsearch.
    """
    doc = {
        'timestamp': datetime.now(),
        'systemPerformanceData': systemPerformanceData
    }
    res = es.index(index="system-performance", doc_type='text', body=doc)
    logging.info(f"System performance data logged with ID: {res['_id']}")

def log_user_feedback(userFeedbackData):
    """
    Logs user feedback data to Elasticsearch.
    """
    doc = {
        'timestamp': datetime.now(),
        'userFeedbackData': userFeedbackData
    }
    res = es.index(index="user-feedback", doc_type='text', body=doc)
    logging.info(f"User feedback data logged with ID: {res['_id']}")

def log_user_activity(userData):
    """
    Logs user activity data to Elasticsearch.
    """
    doc = {
        'timestamp': datetime.now(),
        'userData': userData
    }
    res = es.index(index="user-activity", doc_type='text', body=doc)
    logging.info(f"User activity data logged with ID: {res['_id']}")

def get_system_performance_logs():
    """
    Retrieves system performance logs from Elasticsearch.
    """
    res = es.search(index="system-performance", body={"query": {"match_all": {}}})
    return res['hits']['hits']

def get_user_feedback_logs():
    """
    Retrieves user feedback logs from Elasticsearch.
    """
    res = es.search(index="user-feedback", body={"query": {"match_all": {}}})
    return res['hits']['hits']

def get_user_activity_logs():
    """
    Retrieves user activity logs from Elasticsearch.
    """
    res = es.search(index="user-activity", body={"query": {"match_all": {}}})
    return res['hits']['hits']
```