from abc import ABC
from Position import Position

class Colonist(ABC):
    def __init__(self):
        super().__init__()
        self.position = None