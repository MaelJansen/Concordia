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

    def __init__(self, order, my_diety, my_personality, card_cost, sale_cost, sale_cost_diplomat):
        self.order = order
        self.my_diety = my_diety
        self.my_personality = my_personality
        self.card_cost = card_cost
        self.sale_cost = sale_cost
        self.sale_cost_diplomat = sale_cost_diplomat
        
    def play_effect(self):
        """
        Parameters
        ----------
        player : Player
            the player who plays the card
        """
        if self.my_personality:
            self.my_personality.personality_action()
        else:
            print("This card has no associated personality action.")
        
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

    def point_calculation(self, player : object, map : Map):
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