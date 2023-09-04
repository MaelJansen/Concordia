import unittest
import typing
from src.Personality import Personality
from src.Personality import Architect
from src.Personality import Colonist_
from src.Personality import Concordia
from src.Personality import Consul
from src.Personality import Diplomat
from src.Personality import Mercator
from src.Personality import Prefect
from src.Personality import PrefectusMagnus
from src.Personality import Senator
from src.Personality import Specialist
from src.Personality import Tribune

from src.Player import Player, StoreHouse
from src.Card import Card, MarketPlace


class PersonalityTest:
    pass


class ArchitectTest:
    pass


class Colonist_Test:
    pass


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
    pass


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
    pass


class TribuneTest:
    pass
