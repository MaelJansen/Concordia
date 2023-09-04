from abc import ABC, abstractmethod
from Piece import Ressource, Colonist
from Player import Player
from enum import Enum


class Personality(ABC):
    def __init__(self):
        self.name = self.__class__.__name__.replace('_', '')
        self.card_action = None
        self.card_example = None

    def __init__(self, name: str, card_action: str, card_example: str):
        self.name = name
        self.card_example = card_example
        self.card_action = card_action

    @abstractmethod
    def personality_action(self, player: Player):
        pass


class Architect(Personality):
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        # Function who ask the player what colons to move and move they colons
        player.move_colonists()

        # Function who build a house in a city
        player.build_houses()
        pass


class Colonist(Personality):
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        # We need to ask the player what he wants to do
        choice_add_colon = True
        if choice_add_colon:
            # A function who can demand what colons to add
            player.add_colons()
        else:
            player.gain_money(5 + player.my_colonist.__sizeof__())


class Concordia(Personality):
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        pass


class Consul(Personality):
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        # Ask the player to buy a card in market without additional cost
        player.buy_in_market(False)


class Diplomat(Personality):
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        # Ask the player to choice another discard's player
        # and play the card on the top of this discard
        pass


class Mercator(Personality):
    was_buy = False

    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        player_finish = False
        if self.was_buy:
            player.gain_money(5)
        else:
            player.gain_money(3)
        while not player_finish:
            # Ask what the player wants to sell
            player.sell()
            # Ask what the player wants to sell
            player.buy()
            player_finish = player.finish_deal()


class Prefect(Personality):
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        want_goods = False
        if want_goods:
            player.get_good_province()
        else:
            player.get_money()
        pass


class PrefectusMagnus(Personality):
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        pass


class Senator(Personality):
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        player.buy_card(2)
        pass


class Specialist(Personality):
    def __init__(self, type_spec: Ressource):
        super().__init__()
        self.name = None
        self.type = type_spec

    def personality_action(self, player: Player):
        player.gain_ressource(self.type)
        pass


class Tribune(Personality):
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        nb_carte_added = player.take_all_defause()
        money_earned = nb_carte_added - 3
        if money_earned > 0:
            player.gain_money(money_earned)
        pass


class Concordia(Personality):
    def ___init___(self):
        super().__init__()

    def personality_action(self, player: Player):
        pass
