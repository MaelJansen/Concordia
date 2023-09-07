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
    def __init__(self, name, min_player, max_player):
        self.name = name
        self.min_player = min_player
        self.max_player = max_player
        self.my_provinces = []
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
        self.my_cities = []
        self.ressource_bonus = my_ressource_bonus
        self.side_resource_bonus = True

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
    def __init__(self, my_assigned_city_token, myName, myX, myY):
        super().__init__()
        self.road_list = ()
        self.assigned_city_token = my_assigned_city_token
        self.name = myName
        self.roman_char = None
        self.x = myX
        self.y = myY
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
        self.roman_char = None
        self.n_copies = None
        self.assigned_resource = None

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
    def __init__(self, firstCity, secondCity, myWayName):
        super().__init__()
        self.city_list = (firstCity, secondCity)
        self.line_way = Way(myWayName)

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