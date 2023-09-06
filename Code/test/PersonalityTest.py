import unittest
import typing

from src.Card import Card, MarketPlace
from Personalities import *
from Players import *
from Code.src.Map import *

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

class Colonist_Test:
    
 def test_colonist(self):
    player: Player = Player(0, 0, (12, 14, 15))
    city: City = City("I", (12, 14, 15))

    city.add_house(player)

    player.my_store_house = ({"wheat": 1, "tools": 1})

    colonist_count: int = 2 
    for _ in range(colonist_count):
        colonist: Colonist = Colonist("Colonist", "Colonist", None)
        player.add_card(colonist)

    colonist.personality_action()

    expected_sesterces: int = 5 + colonist_count  
    self.assertEqual(player.get_sesterces(), expected_sesterces)

class ConcordiaTest:
    pass


class ConsulTest:
    def test_consul(self):
        consul: Consul = Consul()

        player_test: Player = Player()
        
        nb_cards_before: int = len(player_test.hand)
        card: Card = Card()

        consul.personality_action(player_test, card)
        nb_cards_after = len(player_test.hand)

        self.assertEqual(nb_cards_after, nb_cards_before + 1)


class DiplomatTest:
    def test_diplomat(self):
        diplomat: Diplomat = Diplomat()

        player1: Player = Player()
        player2: Player = Player()

        test_card: Card = Card()
        player2.discard_pile.append(test_card)

        diplomat.personality_action(player2)

        self.assertIn(diplomat, player1.discard_pile)


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
    def test_perfect(self): 
        player: Player = Player(0, 0, (12, 14, 15))
        province: Province = Province("I", (12, 14, 15))

        player.add_province_token(province)

        choice: str = "bonuses_and_products"  

        player.return_province_token(choice)

        if choice == "bonuses_and_products":
            expected_bonuses = {"wood": 2, "clay": 1, "wheat": 3}  
            expected_products = {"wood": 4, "clay": 2, "wheat": 5}  
            self.assertEqual(player.get_production_bonuses(), expected_bonuses)
            self.assertEqual(player.get_province_products(), expected_products)
        elif choice == "coins":
            for province in player.get_provinces():
                self.assertTrue(province.is_active())
            expected_coins: int = 10  
            self.assertEqual(player.get_sesterces(), expected_coins)


class PrefectusMagnusTest:
    pass


class SenatorTest:
    def test_senator(self):
        senator: Senator = Senator()

        player: Player = Player()

        card1: Card = Card()
        card2: Card = Card()

        marketplace: MarketPlace = MarketPlace()

        senator.personality_action(player, card1, card2)

        self.assertIn(card1, player.discard_pile)
        self.assertIn(card2, player.discard_pile)

        self.assertNotIn(card1, marketplace.display_area)
        self.assertNotIn(card2, marketplace.display_area)


class SpecialistTest:
    def test_specialist(self):
        specialist: Specialist = Specialist("Mason","Specialist",null)
        
        player: Player = Player(0,0, (12,14,15)) 
        player.add_card(specialist)
        
        city: City = City("I", (12,14,15))
        city.add_house(player)
        
        specialist.personality_action()
        self.assertEqual(player.my_store_house[0].type, "brick")
        
        
    def test_specialist2(self):
        specialist: Specialist = Specialist("Mason","Specialist",null)
        
        player: Player = Player(0,0, (12,14,15)) 
        player.add_card(specialist)
        
        city: City = City("I", (12,14,15))
        city.add_house(player)
        
        specialist.personality_action()
        self.assertEqual(player.my_store_house[0].type, "brick")
        
        specialist.personality_action()
        self.assertEqual(player.my_store_house[1].type, null)


class TribuneTest:
    pass
