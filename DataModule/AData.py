from abc import ABC, abstractmethod
from typing import Optional
from .DataSet import DataSet
from .Coord import Coord
import os
import csv
import random

class AData(ABC):
    def __init__(self, filePath: str) -> None :
        self.__filePath: str = 'DataSet/' + filePath + '.csv'
        if not os.path.exists(self.__filePath):
            raise Exception("Data set" + self.__filePath + " not found")

    def extractByCoord(self, vec2: Coord, size: int = 5) -> list[dict]:
        with open(self.__filePath, "r") as f:
            set = csv.reader(f)
            headers = next(set)
            longitude_index = next((i for i, header in enumerate(headers) if 'longitude' in header.lower()), None)
            latitude_index = next((i for i, header in enumerate(headers) if 'latitude' in header.lower()), None)
            finds = sorted([(Coord.distance(Coord(float(row[longitude_index]), float(row[latitude_index])), vec2), row) for row in set],  key=lambda x: x[0])[:size]
            type: object = self.dataSetType
            prompts: list[DataSet] = [str(type(**self.__formatType(headers, data[1], data[0]))) for data in finds]
        return [
            {"prompt": prompt, "valid": True, "points": type.points()}  for prompt in prompts
        ]

    def extractRandom(self, size = 5) -> list[dict]:
        with open(self.__filePath, "r") as f:
            data_reader = csv.reader(f)
            headers = next(data_reader)
            # Read all data rows
            data = list(data_reader)
            # Randomly select size number of rows
            random_rows = random.sample(data, min(size, len(data)))
            # Format the selected rows into DataSet objects
            type: object = self.dataSetType
            prompts: list[DataSet] = [str(type(**self.__formatType(headers, row, None))) for row in random_rows]
        return [
            {"prompt": prompt, "valid": False, "points": type.points()} for prompt in prompts
        ]

    @staticmethod
    def __formatType(headers: list[str], row: list[str], distance: Optional[float]) -> dict:
        base: dict =  {
            header.lower(): row[i] for i, header in enumerate(headers) if header not in ['longitude', 'latitude']
        }
        base.update({"distance": distance})
        return base

    @property
    def dataSetType(self) -> DataSet:
        return self.__dataSetType

