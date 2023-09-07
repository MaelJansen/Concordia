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
    peaceful_end : bool
    Methods
    -------

    """
    def __init__(self):
        self.n_point = 0
        self.money = 0
        self.color = ()
        self.my_store_house = StoreHouse()
        self.my_colonist = []
        self.discard_pile = []
        self.hand = []
        self.my_houses = []
        self.peaceful_end = False
        
    def play_card(self, card: Card):
        """
        Parameters
        ----------
        card : Card
            the card to play
        """
        if card in self.hand:
            card.play_effect()
            self.hand.remove(card)
            self.discard_pile.append(card)
        else:
            print("The card is not in your hand.")

class StoreHouse:
    def __init__(self):
        self.my_pieces = []