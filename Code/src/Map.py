from abc import ABC, abstractmethod
#from Piece import Ressource

class Map:
    """
    The class to represent the map

    ...

    Attributes
    ----------
    name : string
    min_player : int
    max_player : int
    map_provinces : Province
    all_positions : Position

    Methods
    -------

    """
    def __init__(self, min_player, map_player):
        self.name = None
        self.min_player = min_player
        self.map_player = map_player
        self.my_provinces = Province()
        self.all_positions = Position()

class Province:
    """
    A class to represent the provinces (place which will contain the cities)

    ...

    Attributes
    ----------
    color : Tuple
    provicnce_cities : List<City>
    resource_bonus : Resource

    Methods
    -------

    """
    def __init__(self, my_ressource_bonus):
        self.color = ()
        self.my_cities = City()
        self.ressource_bonus = my_ressource_bonus

class Position(ABC):
    """
    A class to stock the coordinates

    ...

    Attributes
    ----------

    Methods
    -------

    """
    def __init__(self):
        pass

class City(Position):
    """
    A class to represent the cities and their resources

    ...

    Attributes
    ----------
    road_list : List<Line>
    assigned_city_token : CityToken
    roman_char : string
    x : int
    y : int
    z : int

    Methods
    -------

    """
    def __init__(self, my_assigned_city_token):
        super().__init__()
        self.road_list = ()
        self.assigned_city_token = my_assigned_city_token
        self.roman_char = None
        self.x = None
        self.y = None
        self.z = None

class CityToken:
    """
    A class to represent the CityToken

    ...

    Attributes
    ----------
    roman_char : string
    n_copies : int
    assigned_resource : Resource

    Methods
    -------

    """
    def __init__(self):
        roman_char = None
        n_copies = None
        assigned_ressource = None

class Line(Position):
    """
    A class to represent the Line (to relate cities between each other)
    ...

    Attributes
    ----------
    city_list : List<City>
    line_way : Way

    Methods
    -------

    """
    def __init__(self):
        super().__init__()
        self.city_list = ()
        self.line_way = Way()

class Way:
    """
    A class to represent the way that will be used by the colonist to travel across the map

    ...

    Attributes
    ----------
    color : Tuple
    max_colonist : int
    n_colonist : int
    name : string

    Methods
    -------
    is_valid_move_for_colonist(self, colonist)

    """
    def __init__(self):
        self.color = None
        self.max_colonist = None
        self.n_colonist = None
        self.name = None
        

python

class Way:
    """
    A class to represent a way or path in the game Concordia.

    Attributes
    ----------
    name : str
        The name of the way.
    occupant : Colonist
        The colonist currently occupying the way (if any).

    Methods
    -------
    __init__(self, name)
        Initializes a new instance of the Way class with the specified name.
    is_valid_move_for_colonist(self, colonist)
        Checks if the move is valid for the given colonist.

    """
    def __init__(self, name):
        self.name = name
        self.occupant = None

    def is_valid_move_for_colonist(self, colonist):
        if self.occupant is not None:
            return False
        
        if colonist.type != self.name:
            return False
        
        return True