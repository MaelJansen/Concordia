from abc import ABC, abstractmethod
from Map import Position, Way

class Piece(ABC):
    """
    A class to represent the piece (resource and colonist)

    ...

    Attributes
    ----------

    Methods
    -------

    """
    def __init__(self):
        pass

class Colonist(Piece):
    """
    A class to represent the colonist

    ...

    Attributes
    ----------
    type : string
    color : tuple
    colonist_way : Way

    Methods
    -------

    """
    def __init__(self):
        super().__init__()
        self.type = None
        self.color = None
        self.colonist_way = Way()

class Ressource(ABC):
    """
    A class to represent the resources

    ...

    Attributes
    ----------
    price : List<Resources>
    bonus_value : int
    type : string
    build_cost : List<>
    color : tuple
    name : string
    Methods
    -------

    """
    def __init__(self, ressource_price, ressource_bonus_value):
        super().__init__()
        self.price = ressource_price
        self.bonus_value = ressource_bonus_value
        self.type = None
        self.build_cost = None
        self.color = None
        self.name = None