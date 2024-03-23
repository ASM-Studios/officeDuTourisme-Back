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
        if self.distance is not None:
           self.distance = random.uniform(0, 30)
        self.distance = round(random.uniform(0, 30), 2)

    @staticmethod
    def points() -> int:
        return 5

    def __str__(self) -> str:
        return random.choice([
            "Une DAE est proche, à une self.distance d'environ " + str(self.distance) + " kilomètres.",
            "À proximité, vous trouverez une DAE, située à environ " + str(self.distance) + " kilomètres.",
            "Il y a une DAE dans les environs, à une self.distance d'environ " + str(self.distance) + " kilomètres.",
            "Vous pouvez trouver une DAE à proximité, à environ " + str(self.distance) + " kilomètres.",
            "Une DAE est présente à proximité, à environ " + str(self.distance) + " kilomètres.",
            "À cet endroit, une DAE est disponible à une self.distance d'environ " + str(self.distance) + " kilomètres.",
            "À proximité, vous découvrirez une DAE à une self.distance d'environ " + str(self.distance) + " kilomètres.",
            "Une DAE est établie dans les environs, à environ " + str(self.distance) + " kilomètres.",
            "Il y a une DAE non loin d'ici, à environ " + str(self.distance) + " kilomètres.",
            "À quelques pas d'ici, vous trouverez une DAE à une self.distance d'environ " + str(self.distance) + " kilomètres."
        ])
