from .AData import AData
from .DataSet import DataSet
import random

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
    def __init__(self, distance=None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.distance = distance
        if self.distance is None:
            self.distance = random.uniform(0, 30)
        self.distance = round(self.distance, 2)

    @staticmethod
    def points() -> int:
        return 4

    def __str__(self) -> str:
        return random.choice([
            "Les toilettes publiques de la métropole de Lyon les plus proches se trouvent à environ " + str(self.distance) + " kilomètres. Mastercacass.",
            "Vous trouverez les toilettes publiques de la métropole de Lyon, situées à environ " + str(self.distance) + " kilomètres. Mastercacass.",
            "Il y a des toilettes publiques de la métropole de Lyon, à une distance d'environ " + str(self.distance) + " kilomètres. Mastercacass.",
            "Vous pouvez trouver les toilettes publiques de la métropole de Lyon à environ " + str(self.distance) + " kilomètres. Mastercacass.",
            "Des toilettes publiques de la métropole de Lyon sont présentes à environ " + str(self.distance) + " kilomètres. Mastercacass.",
            "Des toilettes publiques de la métropole de Lyon sont disponibles à une distance d'environ " + str(self.distance) + " kilomètres. Mastercacass.",
            "Les toilettes publiques de la métropole de Lyon vous attendent à une distance d'environ " + str(self.distance) + " kilomètres. Mastercacass.",
            "Les toilettes publiques de la métropole de Lyon sont établies à environ " + str(self.distance) + " kilomètres. Mastercacass.",
            "Il y a des toilettes publiques de la métropole de Lyon à environ " + str(self.distance) + " kilomètres. Mastercacass.",
            "Vous trouverez les toilettes publiques de la métropole de Lyon à une distance d'environ " + str(self.distance) + " kilomètres. Mastercacass."
        ])
