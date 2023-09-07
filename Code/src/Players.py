from .Pieces import Piece, Colonist
from .Cards import Card
from .Map import Map, City

class Player:
    """
    A class to represent the players

    ...

    Attributes
    ----------
    n_point : int
    money : int
    color : tuple
    my_store_house : StoreHouse
    player_colonist : Colonist
    house : City
    discard_pile : List<Card>
    hand : List<Card>
    Methods
    -------

    """
    def __init__(self):
        self.n_point = 0
        self.money = 0
        self.color = ()
        self.my_store_house = StoreHouse()
        self.my_colonist = []
        self.house = []
        self.discard_pile = []
        self.hand = []
        self.my_houses = []

    def play_card(self, card: Card):
        """ Play a card ( and her effect)

        Args:
        card (Cards): the card who the player want to play
        """
        card.play_effect()

class StoreHouse:
    def __init__(self):
        self.my_pieces = []