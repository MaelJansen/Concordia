from abc import ABC, abstractmethod
from Map import Position

class Piece(ABC):
    def __init__(self):
        pass

class Colonist(Piece):
    def __init__(self):
        super().__init__()
        self.position = None

class Ressource(ABC):
    def __init__(self, ressource_price, ressource_bonus_value):
        super().__init__()
        self.price = ressource_price
        self.bonus_value = ressource_bonus_value
        self.type = None

    def bonus_value(type_ressource):
        pass

    def price_value(type_ressource):
        pass

