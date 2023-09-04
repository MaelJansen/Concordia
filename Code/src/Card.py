from Personality import Personality

class Card:
    """
    A class to represent the cards

    ...

    Attributes
    ----------
    order : int
    card_diety : God
    card_personality : Personality
    sale_cost : int
    sale_cost_diplomat : int

    Methods
    -------

    """
    def __init__(self):
        self.order = None
        self.my_diety = None
        self.my_personality = None
        self.sale_cost = None
        self.sale_cost_diplomat = None

class God:
    """
    A class to represent the
    gods and do the point calculation at the end of the game

    ...

    Attributes
    ----------
    name : string
    signiificance : string
    rewards : string
    example : string
    victory_points : int

    Methods
    -------
    point_calcultation(player : Player)
        Calculate the victory points for each gods
    """
    def __init__(self, diety_name):
        self.name = diety_name
        self.significance = None
        self.rewards = None
        self.example = None
        self.victory_points = None

    def point_calculation(player):
        pass

class MarketPlace:
    """
    A class to represent the market place

    ...

    Attributes
    ----------
    stack : List<Card>
    display_area : List<Card>

    Methods
    -------

    """
    def __init__(self):
        self.stack = ()
        self.display_area = ()

class Numeral:
    """
    A class to represent the value of roman number

    ...

    Attributes
    ----------
    value : int
    roman_number : string

    Methods
    -------

    """
    def __init__(self):
        self.value = None
        self.roman_number = None