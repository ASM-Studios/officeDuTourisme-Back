import random

class DAEDataSet(DataSet):
    def __init__(self, distance=None, **kwargs) -> None:
        super().__init__(**kwargs)
        if distance is not None:
            self.distance = distance
        else:
            self.distance = round(random.uniform(0, 30), 2)

    @staticmethod
    def points() -> int:
        return 5

    def __str__(self) -> str:
        distance = round(random.uniform(0, 30), 2)
        return random.choice([
            "Une DAE est proche, à une distance d'environ " + str(distance) + " kilomètres.",
            "À proximité, vous trouverez une DAE, située à environ " + str(distance) + " kilomètres.",
            "Il y a une DAE dans les environs, à une distance d'environ " + str(distance) + " kilomètres.",
            "Vous pouvez trouver une DAE à proximité, à environ " + str(distance) + " kilomètres.",
            "Une DAE est présente à proximité, à environ " + str(distance) + " kilomètres.",
            "À cet endroit, une DAE est disponible à une distance d'environ " + str(distance) + " kilomètres.",
            "À proximité, vous découvrirez une DAE à une distance d'environ " + str(distance) + " kilomètres.",
            "Une DAE est établie dans les environs, à environ " + str(distance) + " kilomètres.",
            "Il y a une DAE non loin d'ici, à environ " + str(distance) + " kilomètres.",
            "À quelques pas d'ici, vous trouverez une DAE à une distance d'environ " + str(distance) + " kilomètres."
        ])
