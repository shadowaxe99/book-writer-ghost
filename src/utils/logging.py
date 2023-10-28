```python
import logging

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# setup logger for system performance data
systemPerformanceLogger = setup_logger('system_performance', 'logs/system_performance.log')

# setup logger for user feedback data
userFeedbackLogger = setup_logger('user_feedback', 'logs/user_feedback.log')

def log_system_performance(data):
    systemPerformanceLogger.info(data)

def log_user_feedback(data):
    userFeedbackLogger.info(data)
```