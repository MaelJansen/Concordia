import unittest
import typing
from Code.src.Personality import Personality
from Code.src.Personality import Architect
from Code.src.Personality import Mercator
from Code.src.Personality import Ressource
from Code.src.Player import Player


class PersonalityTest:
    pass


class ArchitectTest:
    def test_architect(self):
        player1 = Player(0, 3, 0, (0, 0, 0))
        Architect.personality_action(player1)
        self.assertEqual(player1.colons, 3)
        self.assertEqual(player1.house, 3)

        player2 = Player(8, 2, 1, (255, 255, 0))
        Architect.personality_action(player2)
        self.assertEqual(player2.colons, 2)
        self.assertEqual(player2.house, 3)

        player3 = Player(0, 2, 0, (0, 0, 0))
        Architect.personality_action(player3)
        self.assertEqual(player3.colons, 1)
        self.assertEqual(player3.house, 1)


class Co    lonist_Test:
    pass


class ConcordiaTest:
    pass


class ConsulTest:
    pass


class DiplomatTest:
    pass


class MercatorTest:
    """
    Test the mercator personality
    """
    def test_mercator(self):
        player: Player = Player(0, 0, (0, 0, 0))
        Mercator.personality_action(player)
        self.assertEqual(player.money, 5)

        player2: Player = Player(8, 5, (255, 255, 0))
        Mercator.personality_action(player2)
        self.assertEqual(player2.money, 10)


class PrefectTest:
    pass


class PrefectusMagnusTest:
    pass


class SenatorTest:
    pass


class SpecialistTest:
    pass


class TribuneTest:
    pass
