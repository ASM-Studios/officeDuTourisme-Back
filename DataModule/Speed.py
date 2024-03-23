from .AData import AData
from .DataSet import DataSet
import random

class Speed(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = SpeedDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class SpeedDataSet(DataSet):
    def __init__(self, distance=None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.distance = distance
        if self.distance is None:
            self.distance = round(random.uniform(0, 30), 2)

    @staticmethod
    @property
    def points() -> int:
        return 2

    def __str__(self) -> str:
        return random.choice([
            "Il y a eu un excès de vitesse à une distance d'environ " + str(self.distance) + " kilomètres d'ici, le " + self.datre + ".",
            "Un excès de vitesse a été enregistré à proximité, à une distance d'environ " + str(self.distance) + " kilomètres d'ici, le " + self.datre + ".",
            "Sur la route, à environ " + str(self.distance) + " kilomètres d'ici, un excès de vitesse a été constaté le " + self.datre + ".",
            "À moins de " + str(self.distance) + " kilomètres d'ici, un excès de vitesse a été observé le " + self.datre + ".",
            "Le " + self.datre + ", un excès de vitesse a été relevé à une distance d'environ " + str(self.distance) + " kilomètres d'ici.",
            "Un excès de vitesse a été détecté sur la route, à une distance d'environ " + str(self.distance) + " kilomètres d'ici, le " + self.datre + ".",
            "À proximité, le " + self.datre + ", un excès de vitesse a été enregistré à environ " + str(self.distance) + " kilomètres d'ici.",
            "Un excès de vitesse a été constaté à une distance d'environ " + str(self.distance) + " kilomètres d'ici, le " + self.datre + ".",
            "Le " + self.datre + ", sur la route à proximité, un excès de vitesse a été repéré à environ " + str(self.distance) + " kilomètres d'ici.",
            "À environ " + str(self.distance) + " kilomètres d'ici, un excès de vitesse a été signalé le " + self.datre + "."
        ])
