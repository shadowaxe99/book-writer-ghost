```python
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalysisModel:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        sentiment_scores = self.analyzer.polarity_scores(text)
        return sentiment_scores

    def get_emotional_context(self, text):
        sentiment_scores = self.analyze_sentiment(text)
        max_score = max(sentiment_scores, key=sentiment_scores.get)
        return max_score
```