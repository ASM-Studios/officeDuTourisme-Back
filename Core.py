from DataModule import (
    AData,
    Hair,
    StarHouse,
    PoopSanctuary,
    AVP,
    Seveso,
    Radar,
    Blood,
    VaccinCenter,
    Blood,
    FiveG,
    Speed,
)
from DataModule import Coord
import random


class Core:
    def __init__(self, *args) -> None:
        self.__datasets: list[AData] = [
            Hair('Hair'),
            StarHouse('StarHouse'),
            PoopSanctuary('PoopSanctuary'),
            AVP('AVP'),
            Blood('Blood'),
            FiveG('FiveG'),
            Speed('Speed'),
            AVP('AVP'),
            Seveso('Seveso'),
            Radar('Radar'),
            Blood('Blood'),
            VaccinCenter('VaccinCenter')
        ]

    def getByCoord(self, vec: dict) -> dict:
        valids = []
        unvalids = []
        total = []
        vec = Coord(float(vec['lng']), float(vec['lat']))
        random.shuffle(self.__datasets)
        random.shuffle([valids.extend(e.extractByCoord(vec)) for e in self.__datasets])
        random.shuffle(self.__datasets)
        random.shuffle([unvalids.extend(e.extractRandom()) for e in self.__datasets])
        valids.extend(unvalids)
        random.shuffle(valids)
        return valids[:(random.randint(4, 7))]
