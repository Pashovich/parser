from .tokens import TokenSpecialCase
from model import ModelLoader
from copy import deepcopy

class SpacyParser():
    nounDependencies = []
    adjectiveDependencies = []
    dataStructure = {}

    def __init__(self, modelLoader : ModelLoader):
        self._model = modelLoader.model
        tempData = modelLoader.loadProperties()
        self.nounDependencies = tempData['nounDependencies']
        self.adjectiveDependencies = tempData['adjectiveDependencies']
        self.dataStructure = tempData['dataStructure']
        del tempData

    def __findDependence(self, token, deps, pos):
        for child in token.children:
            if child.dep_ in deps and child.pos_ in pos:
                return child
        return TokenSpecialCase()

    def __checkDuplicates(self, token, data):
        for item in data:
            if item['object'] == token.text:
                return False
        return True

    def parse(self, sentence: str):
        data = list()
        doc = self._model(sentence)
        for token in doc:
            if token.dep_ == 'ROOT':
                dto = deepcopy(self.dataStructure)
                dto['action'] = token.text

                tempObject = self.__findDependence(token, self.nounDependencies, ['NOUN'])
                dto['object'] = tempObject.text

                tempProperty = self.__findDependence(tempObject, self.adjectiveDependencies, ['ADJ'])
                dto['property'] = tempProperty.text

                data.append(dto)

            if token.dep_ in self.nounDependencies and self.__checkDuplicates(token, data):
                dto = deepcopy(self.dataStructure)
                dto['object'] = token.text
                tempProperty = self.__findDependence(token, self.adjectiveDependencies, ['ADJ'])
                dto['property'] = tempProperty.text
                data.append(dto)
        return data
