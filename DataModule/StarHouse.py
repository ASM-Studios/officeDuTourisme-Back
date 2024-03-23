from .AData import AData
from .DataSet import DataSet
import random

class StarHouse(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = StarHouseDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType


    def abs(self) -> None:
        pass

class StarHouseDataSet(DataSet):
    def __init__(self, distance=None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.distance = distance
        if self.distance is None:
            self.distance = random.uniform(0, 30)
        self.distance = round(self.distance, 2)

    @staticmethod
    def points() -> int:
        return 3

    def __str__(self) -> str:
        return random.choice([
            "A " + str(self.distance) + ", cet endroit était le lieu de résidence de l'éminent " + self.prompt + ".",
            "A " + str(self.distance) + ", a vécu l'illustre " + self.prompt + ".",
            "A " + str(self.distance) + ", c'est ici que l'illustre " + self.prompt + " avait élu domicile.",
            "A " + str(self.distance) + ", l'éminent " + self.prompt + " a résidé en ce lieu.",
            "A " + str(self.distance) + ", nous retrouvons la demeure de l'illustre " + self.prompt + ".",
            "L'illustre " + self.prompt + " avait choisi de vivre à", str(self.distance), " d'ici."
            "A " + str(self.distance) + ", c'est ici que résidait l'éminent " + self.prompt + ".",
            "A " + str(self.distance) + ", en ce lieu, a vécu l'illustre " + self.prompt + ".",
            "A " + str(self.distance) + ", cet endroit a été la résidence de l'éminent " + self.prompt + ".",
            "A " + str(self.distance) + " résidait l'illustre " + self.prompt + "."
        ])
