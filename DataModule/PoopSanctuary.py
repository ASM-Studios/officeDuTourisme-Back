from .AData import AData
from .DataSet import DataSet
import math

class PoopSanctuary(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = PoopSanctuaryDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class PoopSanctuaryDataSet(DataSet):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __str__(self) -> str:
        return "Les toilettes publiques de la métropôle de Lyon les plus proches sont a " + str(self.distance) + " kms. Mastercacass."