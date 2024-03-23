from .AData import AData
from .DataSet import DataSet
import math

class FiveG(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = FiveGDataSet
        self.__points: int = 2

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    @property
    def points(self) -> int:
        return self.__points

    def abs(self) -> None:
        pass

class FiveGDataSet(DataSet):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __str__(self) -> str:
        return "Vous pouvez récuperer votre dose de vaccin à " + str(self.distance) + " kms. (Antenne 5G)"