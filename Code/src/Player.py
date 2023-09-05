from Code.src.Main import PlayerController
from Piece import Piece, Colonist
from Card import Card, MarketPlace
from Map import City

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

    controller: PlayerController

    def __init__(self):
        self.n_point = 0
        self.money = 0
        self.color = ()
        self.my_store_house = StoreHouse()
        self.my_colonist = []
        self.house = City()
        self.discard_pile = Card()
        self.hand = []
        self.my_houses = []
        self.controller = None


class StoreHouse:
    def __init__(self):
        self.my_pieces = Piece()