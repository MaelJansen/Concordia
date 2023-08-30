from abc import ABC
from City import City

class Line(ABC):
    def __init__(self):
        super().__init__()
        self.city_list = ()