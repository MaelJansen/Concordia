from abc import ABC
from City import City
from Line import Line
from Ressource import Ressource

class City(ABC):
    def __init__(self, my_assigned_ressource):
        super().__init__()
        self.have_one_house = ()
        self.road_list = ()
        self.assigned_ressource = my_assigned_ressource