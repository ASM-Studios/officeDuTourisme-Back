from .AData import AData
from .DataSet import DataSet
from .Coord import Coord
import random

class AVP(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = AVPDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    @staticmethod
    @property
    def points() -> int:
        return 2

class AVPDataSet(DataSet):
    def __init__(self, distance=None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.distance = distance
        if self.distance is None:
            self.distance = random.uniform(0, 30)
        self.distance = round(self.distance, 2)

    @staticmethod
    def points() -> int:
        return 5

    def __str__(self) -> str:
        return random.choice([
            "À moins de " + str(self.distance) + " kilomètres d'ici, un accident impliquant des blessés s'est produit sur la voie publique.",
            "Près d'ici, à une distance d'environ " + str(self.distance) + " kilomètres, un accident corporel a eu lieu sur la voie publique.",
            "Sur la voie publique à moins de " + str(self.distance) + " kilomètres d'ici, il y a eu un accident impliquant des blessés.",
            "À moins de " + str(self.distance) + " kilomètres d'ici, un accident impliquant des blessés s'est produit sur la route.",
            "Un accident corporel s'est produit sur la voie publique, à une distance d'environ " + str(self.distance) + " kilomètres d'ici.",
            "À moins de " + str(self.distance) + " kilomètres d'ici, un incident avec des blessés a eu lieu sur la voie publique.",
            "Il y a eu un accident impliquant des blessés sur la route publique, à environ " + str(self.distance) + " kilomètres d'ici.",
            "À " + str(self.distance) + " kilomètres d'ici, un accident corporel s'est produit sur la voie publique.",
            "Près d'ici, à moins de " + str(self.distance) + " kilomètres, un accident avec des blessés s'est produit sur la route.",
            "Sur la voie publique, à une distance d'environ " + str(self.distance) + " kilomètres d'ici, un accident corporel a été signalé."
        ])
