from Piece import Piece, Colonist
from Card import Card, MarketPlace

class Player:
    def __init__(self):
        self.n_point = 0
        self.money = 0
        self.color = ()
        self.my_store_house = StoreHouse()
        self.my_land_colonists = ()
        self.my_sea_colonists = ()
        self.discard_pile = ()
        self.my_deck = ()

class StoreHouse:
    def __init__(self):
        my_pieces = ()