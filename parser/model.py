import spacy
import json
def singleton(class_):
    instances = dict()

    def instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return instance

@singleton
class ModelLoader:
    def loadModel(self, path):
        self.model = spacy.load(path)
        return self.model

    @staticmethod
    def loadProperties():
        with open('data-types.json') as file:
            return json.load(file)