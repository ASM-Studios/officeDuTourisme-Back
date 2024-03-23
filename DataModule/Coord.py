from typing import Any
from math import sqrt, radians, sin, atan2, cos
import random

class Coord:
    def __init__(self, longitude: float, latitude: float) -> None:
        self.__longitude: float = longitude
        self.__latitude: float = latitude

    @property
    def longitude(self) -> float:
        return self.__longitude

    @property
    def latitude(self) -> float:
        return self.__latitude

    @staticmethod
    def distance(c1, c2) -> float:
        # Rayon moyen de la Terre en kilomètres
        R = 6371.0

        # Conversion des degrés en radians
        lat1, lon1 = radians(c1.latitude), radians(c1.longitude)
        lat2, lon2 = radians(c2.latitude), radians(c2.longitude)

        # Différence de latitude et de longitude
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        # Formule de Haversine
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Distance en kilomètres
        distance = R * c

        return distance

    @staticmethod
    def generateRandom(baseCoord, minimalDistance: float = 100.0):
        max_distance_degrees = minimalDistance / 111.0  # Approximation : 1 degré de latitude ≈ 111 km

        while True:
            lat = baseCoord.latitude + random.uniform(-max_distance_degrees, max_distance_degrees)
            lon = baseCoord.longitude + random.uniform(-max_distance_degrees, max_distance_degrees)

            random_point = Coord(lat, lon)

            distance = baseCoord.distance(baseCoord, random_point)
            if distance >= minimalDistance:
                return random_point

    def __call__(self, *args: Any, **kwds: Any) -> None:
        if args == 2 and isinstance(args[0], float) and isinstance(args[1], float):
            self.__init__(args[0], args[1])
