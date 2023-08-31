from Personality import Personality

class Card:
    def __init__(self):
        self.order = None
        self.my_diety = None
        self.my_personality = None
        self.sale_cost = None
        self.sale_cost_diplomat = None

class God:
    def __init__(self, diety_name):
        self.name = diety_name
        self.significance = None
        self.rewards = None
        self.example = None
        self.victory_points = None

    def point_calculation(player):
        pass

class MarketPlace:
    def __init__(self):
        self.stack = ()
        self.display_area = ()

class Numeral:
    def __init__(self):
        self.value = None
        self.roman_number = None