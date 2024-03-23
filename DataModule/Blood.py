from .AData import AData
from .DataSet import DataSet
import random

class Blood(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = BloodDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class BloodDataSet(DataSet):
    def __init__(self, distance=None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.distance = distance
        if self.distance is None:
            self.distance = round(random.uniform(0, 30), 2)

    @staticmethod
    @property
    def points() -> int:
        return 5

    def __str__(self) -> str:
        return random.choice([
            "À proximité, vous trouverez un centre de collecte de sang situé à environ " + str(self.distance) + " kilomètres.",
            "Un centre de collecte de sang se situe à environ " + str(self.distance) + " kilomètres de cet endroit.",
            "Il y a un centre de collecte de sang dans les environs, à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Vous pouvez trouver un centre de collecte de sang à proximité, à environ " + str(self.distance) + " kilomètres.",
            "Un centre de collecte de sang est présent à proximité, à une distance d'environ " + str(self.distance) + " kilomètres.",
            "À cet endroit, un centre de collecte de sang est disponible à une distance d'environ " + str(self.distance) + " kilomètres.",
            "À proximité, un centre de collecte de sang vous attend à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Un centre de collecte de sang est établi dans les environs, à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Il y a un centre de collecte de sang non loin d'ici, à une distance d'environ " + str(self.distance) + " kilomètres.",
            "À quelques pas d'ici, vous trouverez un centre de collecte de sang situé à environ " + str(self.distance) + " kilomètres."
        ])
