from .AData import AData
from .DataSet import DataSet
import random

class Radar(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = RadarDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class RadarDataSet(DataSet):
    def __init__(self, distance=None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.distance = distance
        if self.distance is None:
            self.distance = round(random.uniform(0, 30), 2)

    @staticmethod
    def points() -> int:
        return 5

    def __str__(self) -> str:
        if self.distance is not None:
            self.distance = random.uniform(0, 30)
        self.distance = round(random.uniform(0, 30), 2)
        return random.choice([
            "À proximité, vous trouverez un radar à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Un radar est situé à proximité de cet endroit, à environ " + str(self.distance) + " kilomètres.",
            "Il y a un radar dans les environs, à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Vous pouvez trouver un radar à proximité, à environ " + str(self.distance) + " kilomètres.",
            "Un radar est présent à proximité, à environ " + str(self.distance) + " kilomètres.",
            "À cet endroit, un radar est disponible à une distance d'environ " + str(self.distance) + " kilomètres.",
            "À proximité, un radar vous attend à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Un radar est établi dans les environs, à environ " + str(self.distance) + " kilomètres.",
            "Il y a un radar non loin d'ici, à environ " + str(self.distance) + " kilomètres.",
            "À quelques pas d'ici, vous trouverez un radar à une distance d'environ " + str(self.distance) + " kilomètres."
        ])
