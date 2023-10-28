```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from sklearn.pipeline import make_pipeline

class CustomMLModel:
    def __init__(self, n_topics=10, n_top_words=10):
        self.n_topics = n_topics
        self.n_top_words = n_top_words
        self.model = None

    def fit(self, data):
        # Use tf-idf features for NMF.
        print("Extracting tf-idf features for NMF...")
        vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')

        # Fit the NMF model
        print(f"Fitting the NMF model (n_topics={self.n_topics}, n_top_words={self.n_top_words})...")
        nmf = NMF(n_components=self.n_topics, random_state=1).fit(data)
        
        self.model = make_pipeline(vectorizer, nmf)

    def transform(self, data):
        return self.model.transform(data)

    def save_model(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)

    def load_model(self, path):
        with open(path, 'rb') as f:
            self.model = pickle.load(f)
```
