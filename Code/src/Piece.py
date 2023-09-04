from abc import ABC, abstractmethod
from Map import Position, Way

class Piece(ABC):
    def __init__(self):
        pass

class Colonist(Piece):
    def __init__(self):
        super().__init__()
        self.type = None
        self.color = None
        self.colonist_way = Way()

class Ressource(ABC):
    def __init__(self, ressource_price, ressource_bonus_value):
        super().__init__()
        self.price = ressource_price
        self.bonus_value = ressource_bonus_value
        self.type = None
        self.build_cost = None
        self.color = None
        self.name = None
        

