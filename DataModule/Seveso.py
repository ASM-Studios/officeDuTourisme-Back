from .AData import AData
from .DataSet import DataSet
import math

class Seveso(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = SevesoDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class SevesoDataSet(DataSet):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @staticmethod
    @property
    def points() -> int:
        return 5

    def __str__(self) -> str:
        return "L'installation seveso " + self.__dict__.get('prompt') + " est proche."
