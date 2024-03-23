from .AData import AData
from .DataSet import DataSet
import math

class Speed(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = SpeedDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class SpeedDataSet(DataSet):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @staticmethod
    @property
    def points() -> int:
        return 2

    def __str__(self) -> str:
        return "le " + self.__dict__.get('date') + ", il y a eu un exces de vitesse à " + str(self.distance) + " d'ici."