from DataModule import (
    AData,
    Hair,
    StarHouse,
    PoopSanctuary,
    AVP
)
from DataModule import Coord


class Core:
    def __init__(self, *args) -> None:
        self.__datasets: list[AData] = [
            Hair('Hair'),
            StarHouse('StarHouse'),
            PoopSanctuary('PoopSanctuary'),
            AVP('AVP')
        ]

    def getByCoord(self, vec: dict) -> dict:
        valids = []
        unvalids = []
        vec = Coord(float(vec['lng']), float(vec['lat']))
        [valids.extend(e.extractByCoord(vec)) for e in self.__datasets]
        [unvalids.extend(e.extractRandom()) for e in self.__datasets]
        valids.extend(unvalids)
        return valids
