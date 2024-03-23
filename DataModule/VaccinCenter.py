from .AData import AData
from .DataSet import DataSet
import random

class VaccinCenter(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = VaccinCenterDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class VaccinCenterDataSet(DataSet):
    def __init__(self, distance=None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.distance = distance
        if self.distance is None:
            self.distance = round(random.uniform(0, 30), 2)

    @staticmethod
    def points() -> int:
        return 5

    def __str__(self) -> str:
        return random.choice([
            "Il y a un centre de vaccination à proximité, à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Un centre de vaccination est situé à proximité de cet endroit, à environ " + str(self.distance) + " kilomètres.",
            "Il y a un centre de vaccination dans les environs, à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Vous pouvez trouver un centre de vaccination à proximité, à environ " + str(self.distance) + " kilomètres.",
            "Un centre de vaccination est présent à proximité, à environ " + str(self.distance) + " kilomètres.",
            "À cet endroit, un centre de vaccination est disponible à une distance d'environ " + str(self.distance) + " kilomètres.",
            "À proximité, un centre de vaccination vous attend à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Un centre de vaccination est établi dans les environs, à environ " + str(self.distance) + " kilomètres.",
            "Il y a un centre de vaccination non loin d'ici, à environ " + str(self.distance) + " kilomètres.",
            "À quelques pas d'ici, vous trouverez un centre de vaccination à une distance d'environ " + str(self.distance) + " kilomètres."
        ])
