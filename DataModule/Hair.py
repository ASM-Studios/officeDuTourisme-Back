from .AData import AData
from .DataSet import DataSet
import random

class Hair(AData):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
        self.__dataSetType: DataSet = HairDataSet

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

    def abs(self) -> None:
        pass

class HairDataSet(DataSet):
    def __init__(self, name, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def __str__(self) -> str:
        return random.choice([
            "Ici, vous trouverez un salon de coiffure portant le nom de " + self.name + ".",
            "Un salon de coiffure, connu sous le nom de " + self.name + ", est situé à cet endroit.",
            "À cet endroit, il y a un salon de coiffure sobrement appelé " + self.name + ".",
            "Vous pouvez trouver un salon de coiffure nommé " + self.name + " à proximité.",
            "Un salon de coiffure, du nom de " + self.name + ", est présent ici.",
            "À cet emplacement, il y a un salon de coiffure sobrement désigné sous le nom de " + self.name + ".",
            "Ici, vous découvrirez un salon de coiffure nommé " + self.name + " de manière simple.",
            "Un salon de coiffure, connu sous le nom de " + self.name + ", est établi ici.",
            "À cet endroit, vous trouverez un salon de coiffure sobrement intitulé " + self.name + ".",
            "Un salon de coiffure portant le nom modeste de " + self.name + " se trouve ici."
        ])
