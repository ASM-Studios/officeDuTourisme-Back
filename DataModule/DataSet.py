from . import Coord

class DataSet():
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    @property
    def coord(self) -> Coord:
        return self.__coord

    def __str__(self) -> str:
        return self.prompt
