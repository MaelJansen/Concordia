from Code.src.Map import City
from Code.src.Cards import Card
from Code.src.Main import PlayerController, GameManager
import unittest
from Code.src.Pieces import Resource
from Code.src.Personalities import *
from Code.src.Players import Player


class GameControllerTest:
    pass


class PlayerControllerTest(unittest.TestCase):

    def test_play(self):
        game: GameManager = GameManager()
        controller: PlayerController = PlayerController()
        player: Player = Player()
        card: Card = Card()
        personality: Architect = Architect(player)
        card.my_personality = personality
        player.hand.append(card)
        controller.play(player, card)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()