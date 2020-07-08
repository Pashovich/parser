import spacy
import json
import os


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
        with open(os.path.join(os.path.dirname(__file__), 'data-types.json'), 'r') as file:
            return json.load(file)
