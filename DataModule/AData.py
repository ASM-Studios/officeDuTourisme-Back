from abc import ABC, abstractmethod

class AData(ABC):
    def __init__(self, filePath: str) -> None :
        self.__filePath: str = filePath

    @abstractmethod
    def abs(self) -> None:
        pass