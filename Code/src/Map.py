from abc import ABC, abstractmethod
#from Piece import Ressource

class Map:
    def __init__(self, min_player, map_player):
        self.min_player = min_player
        self.map_player = map_player
        self.my_provinces = ()

class Province:
    def __init__(self, my_ressource_bonus):
        self.color = ()
        self.my_cities = ()
        self.ressource_bonus = my_ressource_bonus

class Position(ABC):
    def __init__(self):
        pass

class City(Position):
    def __init__(self, my_assigned_city_token):
        super().__init__()
        self.have_one_house = ()
        self.road_list = ()
        self.assigned_city_token = my_assigned_city_token

class CityToken:
    def __init__(self):
        roman_char = None
        n_copies = None
        assigned_ressource = None

class Line(Position):
    def __init__(self):
        super().__init__()
        self.city_list = ()

    