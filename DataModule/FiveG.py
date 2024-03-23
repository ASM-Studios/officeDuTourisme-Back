from .AData import AData
from .DataSet import DataSet
import math

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
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @staticmethod
    @property
    def points() -> int:
        return 2

    def __str__(self) -> str:
        return "Vous pouvez récuperer votre dose de vaccin à " + str(self.distance) + " kms. (Antenne 5G)"