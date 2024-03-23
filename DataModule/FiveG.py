from .AData import AData
from .DataSet import DataSet
import random

class FiveG(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = FiveGDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class FiveGDataSet(DataSet):
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
            "Une antenne 5G est installée à une distance d'environ " + str(self.distance) + " kilomètres d'ici.",
            "À proximité, vous trouverez une antenne 5G située à environ " + str(self.distance) + " kilomètres.",
            "Il y a une antenne 5G dans les environs, à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Vous pouvez trouver une antenne 5G à proximité, à environ " + str(self.distance) + " kilomètres.",
            "Une antenne 5G est présente à proximité, à environ " + str(self.distance) + " kilomètres.",
            "À cet endroit, une antenne 5G est disponible à une distance d'environ " + str(self.distance) + " kilomètres.",
            "À proximité, une antenne 5G vous attend à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Une antenne 5G est établie dans les environs, à environ " + str(self.distance) + " kilomètres.",
            "Il y a une antenne 5G non loin d'ici, à environ " + str(self.distance) + " kilomètres.",
            "À quelques pas d'ici, vous trouverez une antenne 5G à une distance d'environ " + str(self.distance) + " kilomètres."
        ])
