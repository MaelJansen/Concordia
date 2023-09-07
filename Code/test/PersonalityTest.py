import unittest
import typing

from Code.src.Cards import Card, MarketPlace
from Code.src.Personalities import *
from Code.src.Players import *
from Code.src.Map import *


class PersonalityTest(unittest.TestCase):

    def test_could_pay_house(self):
        player = Player()
        city_token: CityToken = CityToken()
        city: City = City(city_token)
        personality: Concordia = Concordia(player)
        self.assertFalse(personality.could_pay_house(city))
        brick = Resource(1, 1, "brick", 1, "blue", "brick")
        city.assigned_city_token.assigned_resource = brick
        self.assertFalse(personality.could_pay_house(city))
        resource: Resource = Resource(1, 1, "food", 1, "green", "food")
        player.my_store_house.my_pieces.append(resource)
        self.assertTrue(personality.could_pay_house(city))
        city.assigned_city_token.assigned_resource = resource
        self.assertFalse(personality.could_pay_house(city))
        player.my_store_house.my_pieces.append(brick)
        self.assertTrue(personality.could_pay_house(city))
        pass

    def test_could_pay(self):
        player = Player()
        personality: Concordia = Concordia(player)
        brick = Resource(1, 1, "brick", 1, "blue", "brick")
        resource: Resource = Resource(1, 1, "food", 1, "green", "food")
        self.assertFalse(personality.could_pay(brick, resource))
        player.my_store_house.my_pieces.append(brick)
        self.assertFalse(personality.could_pay(brick, resource))
        self.assertTrue(personality.could_pay(brick))
        player.my_store_house.my_pieces.append(resource)
        self.assertTrue(personality.could_pay(brick, resource))
        self.assertTrue(personality.could_pay(resource) and personality.could_pay(brick))
        pass

    def test_pay_house(self):
        player = Player()
        city_token: CityToken = CityToken()
        city: City = City(city_token)
        personality: Concordia = Concordia(player)
        brick = Resource(1, 1, "brick", 1, "blue", "brick")
        city.assigned_city_token.assigned_resource = brick
        resource: Resource = Resource(1, 1, "food", 1, "green", "food")
        player.my_store_house.my_pieces.append(resource)
        player.my_store_house.my_pieces.append(brick)
        self.assertTrue(resource in player.my_store_house.my_pieces)
        self.assertTrue(brick in player.my_store_house.my_pieces)
        personality.pay_house(city)
        self.assertTrue(resource not in player.my_store_house.my_pieces)
        player.my_store_house.my_pieces.append(resource)
        city.assigned_city_token.assigned_resource = resource
        personality.pay_house(city)
        self.assertTrue(resource not in player.my_store_house.my_pieces)
        self.assertTrue(brick not in player.my_store_house.my_pieces)
        pass

    def test_pay_with_resource(self):
        player = Player()
        city_token: CityToken = CityToken()
        city: City = City(city_token)
        personality: Concordia = Concordia(player)
        brick = Resource(1, 1, "brick", 1, "blue", "brick")
        city.assigned_city_token.assigned_resource = brick
        resource: Resource = Resource(1, 1, "food", 1, "green", "food")
        player.my_store_house.my_pieces.append(resource)
        player.my_store_house.my_pieces.append(brick)
        self.assertTrue(resource in player.my_store_house.my_pieces)
        self.assertTrue(brick in player.my_store_house.my_pieces)
        personality.pay_with_resource(resource,brick)
        self.assertTrue(resource not in player.my_store_house.my_pieces)
        self.assertTrue(brick not in player.my_store_house.my_pieces)

    def test_pay_with_resource_by_name(self):
        player = Player()
        city_token: CityToken = CityToken()
        city: City = City(city_token)
        personality: Concordia = Concordia(player)
        brick = Resource(1, 1, "brick", 1, "blue", "brick")
        city.assigned_city_token.assigned_resource = brick
        resource: Resource = Resource(1, 1, "food", 1, "green", "food")
        player.my_store_house.my_pieces.append(resource)
        player.my_store_house.my_pieces.append(brick)
        self.assertTrue(resource in player.my_store_house.my_pieces)
        self.assertTrue(brick in player.my_store_house.my_pieces)
        personality.pay_with_resource_by_name("food", "brick")
        self.assertTrue(resource not in player.my_store_house.my_pieces)
        self.assertTrue(brick not in player.my_store_house.my_pieces)


class ArchitectTest(unittest.TestCase):
    def test_architect(self):
        player1 = Player(0, 3, 0, (0, 0, 0))
        Architect.personality_action(player1)
        self.assertEqual(player1.colons, 3)
        self.assertEqual(player1.house, 3)

        player2 = Player(8, 2, 1, (255, 255, 0))
        Architect.personality_action()
        self.assertEqual(len(player2.my_colonist), 2)
        self.assertEqual(player2.house, 3)

        player3 = Player(0, 2, 0, (0, 0, 0))
        Architect.personality_action(player3)
        self.assertEqual(player3.colons, 1)
        self.assertEqual(player3.house, 1)


class Colonist_Test(unittest.TestCase):

    def test_colonist(self):
        test_food = Resource(2, 1, "food", 1, "yellow", "food")
        test_tool = Resource(2, 1, "tool", 1, "blue", "tool")

        player: Player = Player()
        city_token: CityToken = CityToken()
        city: City = City(city_token)

        colonist_test: Colonist_ = Colonist_(player)

        player.my_houses.append(city)

        player.my_store_house.my_pieces.append(test_food)
        player.my_store_house.my_pieces.append(test_tool)

        colonist_count: int = 2
        for _ in range(colonist_count):
            colonist: Colonist = Colonist("ground", "blue")
            player.my_colonist.append(colonist)

        test_colonist: Colonist = Colonist("ground", "blue")

        colonist_test.personality_action(False)

        expected_sesterces: int = 5 + colonist_count
        self.assertEqual(player.money, expected_sesterces)

        colonist_test.personality_action(True,test_colonist)
        self.assertTrue(test_colonist in player.my_colonist)


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


class SenatorTest(unittest.TestCase):
    def test_senator(self):
        player: Player = Player()
        senator: Senator = Senator(player)

        card1: Card = Card()
        card2: Card = Card()

        marketplace: MarketPlace = MarketPlace()
        marketplace.display_area.append(card1)
        marketplace.display_area.append(card2)

        senator.personality_action(card1, card2, marketplace)

        self.assertIn(card1, player.hand)
        self.assertIn(card2, player.hand)

        self.assertNotIn(card1, marketplace.display_area)
        self.assertNotIn(card2, marketplace.display_area)


class SpecialistTest(unittest.TestCase):
    def test_specialist(self):
        test_brick = Resource(2, 1, "brick", 1, "blue", "brick")

        player: Player = Player()
        specialist: Specialist = Specialist(player, test_brick)
        player.hand.append(specialist)

        city_token: CityToken = CityToken()
        city_token.assigned_resource = test_brick
        city: City = City(city_token)
        player.my_houses.append(city)

        self.assertEqual(len(player.my_store_house.my_pieces), 0)
        specialist.personality_action()
        self.assertEqual(player.my_store_house.my_pieces[0], test_brick)

    def test_specialist2(self):
        test_food = Resource(2, 1, "food", 1, "yellow", "food")
        test_brick = Resource(2, 1, "brick", 1, "blue", "brick")

        player: Player = Player()
        specialist: Specialist = Specialist(player, test_food)
        player.hand.append(specialist)

        city_token: CityToken = CityToken()
        city_token.assigned_resource = test_brick
        city: City = City(city_token)
        player.my_houses.append(city)

        specialist.personality_action()
        self.assertEqual(len(player.my_store_house.my_pieces),0)

        city_token: CityToken = CityToken()
        city_token.assigned_resource = test_food
        food_city: City = City(city_token)
        player.my_houses.append(food_city)
        specialist.personality_action()
        self.assertEqual(len(player.my_store_house.my_pieces),1)


class TribuneTest(unittest.TestCase):

    def test_tribune(self):
        test_food = Resource(2, 1, "food", 1, "yellow", "food")

        player: Player = Player()
        specialist: Specialist = Specialist(player, test_food)
        player.discard_pile.append(specialist)

        tribune_test: Tribune = Tribune(player)
        player.hand.append(tribune_test)

        self.assertFalse(specialist in player.hand)
        self.assertTrue(tribune_test in player.hand)
        self.assertEqual(len(player.discard_pile),1)

        tribune_test.personality_action(None)

        self.assertEqual(len(player.discard_pile), 0)
        self.assertEqual(len(player.hand), 2)
        self.assertEqual(player.money, 0,f"{player.money} != 0")
        self.assertTrue(specialist in player.hand)
        self.assertTrue(tribune_test in player.hand)
        pass

    def test_tribune2(self):
        test_food = Resource(2, 1, "food", 1, "yellow", "food")
        test_tool = Resource(2,1,"tool",1,"grey","tool")

        player: Player = Player()
        specialist: Specialist = Specialist(player, test_food)
        player.discard_pile.append(specialist)

        player.my_store_house.my_pieces.append(test_food)

        colonist_test: Colonist = Colonist("ground","blue")

        tribune_test: Tribune = Tribune(player)
        player.hand.append(tribune_test)

        self.assertFalse(specialist in player.hand)
        self.assertTrue(tribune_test in player.hand)
        self.assertEqual(len(player.discard_pile), 1)

        tribune_test.personality_action(colonist_test)

        self.assertFalse(colonist_test in player.my_colonist)
        self.assertTrue(test_food in player.my_store_house.my_pieces)

        player.my_store_house.my_pieces.append(test_tool)
        tribune_test.personality_action(colonist_test)

        self.assertTrue(colonist_test in player.my_colonist)
        self.assertFalse(test_food in player.my_store_house.my_pieces)
        self.assertFalse(test_tool in player.my_store_house.my_pieces)
        pass
