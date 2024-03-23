from .AData import AData
from .DataSet import DataSet
import math

class VaccinCenter(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = VaccinCenterDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class VaccinCenterDataSet(DataSet):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @staticmethod
    def points() -> int:
        return 5

    def __str__(self) -> str:
        return "Il y'a un centre de vaccination a proximité"
