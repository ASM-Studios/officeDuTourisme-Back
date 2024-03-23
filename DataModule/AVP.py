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

class AVPDataSet(DataSet):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __str__(self) -> str:
        if not self.__dict__.get("distance"):
            self.distance = random.uniform(0, 30)
        self.distance = round(self.distance, 2)
        return "Il y a un accident corporel sur la voie publique à moins de " + str(self.distance) + "Km d'ici."