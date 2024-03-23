from .AData import AData
from .DataSet import DataSet
import random

class DAE(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = DAEDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class DAEDataSet(DataSet):
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
            "Une installation Seveso est proche, à une distance d'environ " + str(self.distance) + " kilomètres.",
            "À proximité, vous trouverez une installation Seveso, située à environ " + str(self.distance) + " kilomètres.",
            "Il y a une installation Seveso dans les environs, à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Vous pouvez trouver une installation Seveso à proximité, à environ " + str(self.distance) + " kilomètres.",
            "Une installation Seveso est présente à proximité, à environ " + str(self.distance) + " kilomètres.",
            "À cet endroit, une installation Seveso est disponible à une distance d'environ " + str(self.distance) + " kilomètres.",
            "À proximité, vous découvrirez une installation Seveso à une distance d'environ " + str(self.distance) + " kilomètres.",
            "Une installation Seveso est établie dans les environs, à environ " + str(self.distance) + " kilomètres.",
            "Il y a une installation Seveso non loin d'ici, à environ " + str(self.distance) + " kilomètres.",
            "À quelques pas d'ici, vous trouverez une installation Seveso à une distance d'environ " + str(self.distance) + " kilomètres."
        ])
