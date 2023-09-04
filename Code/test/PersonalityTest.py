import unittest
import typing

from src.Card import Card, MarketPlace
from Code.src.Personality import *
from Code.src.Player import *
from Code.src.Map import *

class PersonalityTest:
    pass


class ArchitectTest:
    pass


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
    # Purchase 1 new personnality card without additionnal costs and put it in your hand
    def test_consul(self):
        consul: Consul = Consul()
        player_test: Player = Player()
        nb_cards_before: int = len(player_test.hand)
        card: Card = Card()
        consul.personality_action(player_test, card)
        nb_cards_after = len(player_test.hand)
        self.assertEqual(nb_cards_after, nb_cards_before + 1)
        return True


class DiplomatTest:
    # Use an opponent's top face up personality card in his discard pile
    def test_diplomat(self):
        # Créez une instance de la classe Diplomat
        diplomat: Diplomat = Diplomat()

        # Créez deux instances de la classe Joueur
        player1: Player = Player()
        player2: Player = Player()

        # Créez une carte de test et ajoutez-la à la défausse du joueur2
        test_card: Card = Card()
        player2.discard_pile.append(test_card)

        # Appelez la méthode qui permet à Diplomat d'utiliser la carte du dessus de la défausse d'un autre joueur
        diplomat.personality_action(player2)

        # Vérifiez que la carte a été utilisée par Diplomat (par exemple, en vérifiant l'état de Diplomat après l'utilisation)
        self.assertIn(diplomat, player1.discard_pile)

        return True


class MercatorTest:
    pass


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
    # Purchase up to 2 new personality and put them into your hand
    def test_senator(self):
        # Créez une instance de la classe Senator
        senator: Senator = Senator()

        # Créez une instance de la classe Joueur
        player: Player = Player()

        # Créez deux cartes de personnalité de test
        card1: Card = Card()
        card2: Card = Card()

        # Créez le marché
        marketplace: MarketPlace = MarketPlace()

        # Appelez la méthode d'achat de cartes de personnalité de Senator
        senator.personality_action(player, card1, card2)

        # Vérifiez que les cartes ont été ajoutées à la main du joueur
        self.assertIn(card1, player.discard_pile)
        self.assertIn(card2, player.discard_pile)

        # Vérifiez que les cartes ont été retirées des cartes de personnalité disponibles dans la partie
        self.assertNotIn(card1, marketplace.display_area)
        self.assertNotIn(card2, marketplace.display_area)

        return True


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
