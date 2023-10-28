```python
import spacy

class NamedEntityRecognitionModel:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_entities(self, text):
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def store_entities(self, entities, interviewData):
        for entity in entities:
            if entity[1] not in interviewData:
                interviewData[entity[1]] = [entity[0]]
            else:
                if entity[0] not in interviewData[entity[1]]:
                    interviewData[entity[1]].append(entity[0])
        return interviewData
```