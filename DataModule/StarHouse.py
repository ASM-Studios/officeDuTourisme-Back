from .AData import AData
from .DataSet import DataSet
import math

class StarHouse(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = StarHouseDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class StarHouseDataSet(DataSet):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __str__(self) -> str:
        return "L'illustre " + self.__dict__.get('prompt') + " a vécu ici."