from Personality import Personality
from Player import Player
from Piece import Ressource
from Map import Map

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
        """
        Parameters
        ----------
        diety_name : str
            the name of the diety
        """
        self.name = diety_name
        self.significance = None
        self.rewards = None
        self.example = None
        self.victory_points = None

    def point_calculation(self, player : Player, map : Map):
        """
        Calculate the player's victory points related to the god

        Parameters
        ----------
        player : Player 
            the player for whom the points are counted
        """
        match self.name:

            case "Vesta":
                for item in player.my_store_house:
                    player.money += item.price
                player.n_point += player.money // 10

            case "Jupiter":
                vp :int = 0
                for houses in player.my_houses:
                    if vp < 15 & houses.assigned_city_token.assigned_ressource != "Brick":
                        vp += 1
                player.n_point += vp

            case "Saturnus":
                conquered_provinces = []
                for provinces in map:
                    for city in provinces:
                        if player.house == city & city not in conquered_provinces:
                            conquered_provinces.append(city)
                player.n_point += len(conquered_provinces)

            case "Mercurius":
                producted_resources : list = []
                for house in player.my_houses:
                    if house.houses.assigned_city_token.assigned_ressource not in producted_resources:
                        producted_resources.append(house.houses.assigned_city_token.assigned_ressource)
                player.n_point += len(producted_resources)*2

            case "Mars":
                n_colonist :int = len(player.my_colonist)
                vp :int = 0
                for stored_colonist in player.my_store_house:
                    if (stored_colonist.type == "colonist"):
                        n_colonist -= 1
                if (n_colonist <= 12):
                    vp = n_colonist
                else:
                    vp = 12
                player.n_point += vp

            case "Minerva":
                player.n_point += 0

            
            
            





            case _:
                #action

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