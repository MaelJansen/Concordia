import Pieces
import Cards
import Map

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
        self.my_colonist = Pieces.Colonist()
        self.house = Map.City()
        self.discard_pile = Cards.Card()
        self.hand = Cards.Card()
        self.my_houses = []

class StoreHouse:
    def __init__(self):
        self.my_pieces = Pieces.Piece()