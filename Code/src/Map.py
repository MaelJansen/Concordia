from abc import ABC, abstractmethod
from Piece import Ressource

class Map:
    def __init__(self, min_player, map_player):
        self.name = None
        self.min_player = min_player
        self.map_player = map_player
        self.my_provinces = Province()
        self.all_positions = Position()

class Province:
    def __init__(self, my_ressource_bonus):
        self.color = ()
        self.my_cities = City()
        self.ressource_bonus = my_ressource_bonus

class Position(ABC):
    def __init__(self):
        pass

class City(Position):
    def __init__(self, my_assigned_city_token):
        super().__init__()
        self.road_list = ()
        self.assigned_city_token = my_assigned_city_token
        self.roman_char = None
        self.x = None
        self.y = None
        self.z = None

class CityToken:
    def __init__(self):
        roman_char = None
        n_copies = None
        assigned_ressource = None

class Line(Position):
    def __init__(self):
        super().__init__()
        self.city_list = ()
        self.line_way = Way()

class Way:
    def __init__(self):
        self.color = None
        self.max_colonist = None
        self.n_colonist = None
        self.name = None



    