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
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @staticmethod
    def points() -> int:
        return 3

    def __str__(self) -> str:
        return random.choice([
            "Cet endroit était le lieu de résidence de l'éminent " + self.prompt + ".",
            "Ici, a vécu l'illustre " + self.prompt + ".",
            "C'est ici que l'illustre " + self.prompt + " avait élu domicile.",
            "L'éminent " + self.prompt + " a résidé en ce lieu.",
            "À cet endroit, nous retrouvons la demeure de l'illustre " + self.prompt + ".",
            "L'illustre " + self.prompt + " avait choisi de vivre ici.",
            "C'est ici que résidait l'éminent " + self.prompt + ".",
            "En ce lieu, a vécu l'illustre " + self.prompt + ".",
            "Cet endroit a été la résidence de l'éminent " + self.prompt + ".",
            "Ici résidait l'illustre " + self.prompt + "."
        ])
