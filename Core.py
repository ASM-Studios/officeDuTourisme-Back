from DataModule import (
    AData,
    Hair,
    StarHouse,
    AVP,
    Seveso,
    Radar,
    Blood,
    VaccinCenter
)
from DataModule import Coord
import random


class Core:
    def __init__(self, *args) -> None:
        self.__datasets: list[AData] = [
            Hair('Hair'),
            StarHouse('StarHouse'),
            AVP('AVP'),
            Seveso('Seveso'),
            Radar('Radar'),
            Blood('Blood'),
            # VaccinCenter('VaccinCenter')
        ]

    def getByCoord(self, vec: dict) -> dict:
        valids = []
        unvalids = []
        total = []
        vec = Coord(float(vec['lng']), float(vec['lat']))
        random.shuffle([valids.extend(e.extractByCoord(vec)) for e in self.__datasets])
        random.shuffle([unvalids.extend(e.extractRandom()) for e in self.__datasets])
        valids.extend(unvalids)
        random.shuffle(valids)
        return valids[:(random.randint(4, 7))]
