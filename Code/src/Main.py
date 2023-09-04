from Player import Player
from Map import Map

class GameManager:
    """
    A class to control the game 

    ...

    Attributes
    ----------
    player_controller : PlayerManager
    game_map : Map
    player_list : List<Player>
    player_color : List<Tuple()>

    Methods
    -------
    initialization_script()
        The method to setup the game

    """
    def __init__(self):
        self.player_controller = PlayerManager()
        self.game_map = Map()
        self.player_list = ()
        self.player_color = None

    def initialization_script():
        pass

class PlayerManager:
    pass