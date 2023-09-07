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
        self.my_colonist = []
        self.discard_pile = []
        self.hand = []
        self.my_houses = []

    def setup_colonists(self,colonist_data):
        """Setup the player colonists according to the database

        Args:
            colonist_data (_type_): _description_
        """
        for i in range (len(colonist_data)):
            type = colonist_data[i][0]
            n_copies = colonist_data[i][2]
            for y in range (0,n_copies-1):
                self.my_store_house.my_pieces.append(Pieces.Colonist(type,self.color))
    
    def setup_goods(self,goods_data):
        print(goods_data)
        for i in range (len(goods_data)):
            type = goods_data[i][0]
            n_copies = goods_data[i][1]
            for y in range (0,n_copies-1):
                self.my_store_house.my_pieces.append(Pieces.Resource(Pieces.ResourceType.RESOURCE_TYPES[type]))

    def setup_houses(self,houses_data):
        pass

    def setup_cards(self,cards_data):
        pass

    def setup_sestertii(self,sestersii_data):
        pass

    def play_card(self, card: Cards.Card):
        """ Play a card ( and her effect)

        Args:
        card (Cards): the card who the player want to play
        """
        card.play_effect()

class StoreHouse:
    def __init__(self):
        self.my_pieces = []