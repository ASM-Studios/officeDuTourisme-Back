from typing import Any

class Coord:
    def __init__(self, longitude: float, latitude: float) -> None:
        self.__longitude: float = longitude
        self.__latitude: float = latitude

    @property
    def longitude(self) -> float:
        self.longitude

    @property
    def latitude(self) -> float:
        self.__latitude

    def __call__(self, *args: Any, **kwds: Any) -> None:
        if args == 2 and isinstance(args[0], float) and isinstance(args[1], float):
            self.__init__(args[0], args[1])
