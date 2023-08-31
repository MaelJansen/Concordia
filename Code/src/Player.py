from Piece import Piece, Colonist
from Card import Card, MarketPlace
from Map import City

class Player:
    def __init__(self):
        self.n_point = 0
        self.money = 0
        self.color = ()
        self.my_store_house = StoreHouse()
        self.my_colonist = Colonist()
        self.house = City()
        self.discard_pile = Card()
        self.hand = Card()

class StoreHouse:
    def __init__(self):
        self.my_pieces = Piece()