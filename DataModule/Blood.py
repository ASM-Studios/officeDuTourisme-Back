from .AData import AData
from .DataSet import DataSet
import random

class Blood(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = BloodDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class BloodDataSet(DataSet):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @staticmethod
    def points() -> int:
        return 5

    def __str__(self) -> str:
        return random.choice([
            "À proximité, vous trouverez un centre de collecte de sang.",
            "Un centre de collecte de sang se situe à proximité de cet endroit.",
            "Il y a un centre de collecte de sang dans les environs.",
            "Vous pouvez trouver un centre de collecte de sang à proximité.",
            "Un centre de collecte de sang est présent à proximité.",
            "À cet endroit, un centre de collecte de sang est disponible.",
            "À proximité, un centre de collecte de sang vous attend.",
            "Un centre de collecte de sang est établi dans les environs.",
            "Il y a un centre de collecte de sang non loin d'ici.",
            "À quelques pas d'ici, vous trouverez un centre de collecte de sang."
        ])
