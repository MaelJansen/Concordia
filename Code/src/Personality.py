from abc import ABC, abstractmethod
from Piece import Ressource
from Player import Player

class Personality(ABC):
    def __init__(self):
        self.name = self.__class__.__name__.replace('_', '')
        self.card_action = None
        self.card_example = None

    @abstractmethod
    def personality_action(self, player: Player):
        pass


class Architect(Personality):
    """
    A class to represent the architect card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch the architect's actions

    """
    def __init__(self):
        super().__init__()
        self.card_action = ""

    def personality_action(self, player: Player):
        # Function who ask the player what colons to move and move they colons
        player.move_colonists()

        # Function who build a house in a city
        player.build_houses()
        pass

class ColonialManager(Personality):
    """
    A class to represent the colonist card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch the colonist's actions

    """
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        # We need to ask the player what he wants to do
        choice_add_colon = True
        if choice_add_colon:
            # A function who can demand what colons to add
            player.add_colons()
        else:
            player.gain_money(5 + player.number_of_colon())


class Concordia(Personality):
    """
    A class to represent Concordia card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch concordia's action

    """
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        pass


class Consul(Personality):
    """
    A class to represent the consul card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch the consul's actions

    """
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        # Ask the player to buy a card in market without additional cost
        player.buy_in_market(False)


class Diplomat(Personality):
    """
    A class to represent the diplomat card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch the diplomat's actions

    """
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        # Ask the player to choice another discard's player
        player_choice: Player = player.choice_discard()
        # and play the card on the top of this discard
        discard_player_choice = player_choice.discard_pile
        discard_player_choice[len(discard_player_choice) - 1].my_personality.personality_action(player)
        pass


class Mercator(Personality):
    """
    A class to represent the Mercator card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch the mercator's action's

    """

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
    """
    A class to represent the prefect card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch the prefect's actions

    """
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
    """
    A class to represent the prefect magnus card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch the prefect magnus's actions

    """
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        pass


class Senator(Personality):
    """
    A class to represent the senator card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch the senator's actions

    """
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        player.buy_card(2)
        pass


class Specialist(Personality):
    """
    A class to represent the specialist card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch the specialist's actions

    """
    def __init__(self, type_spec: Ressource):
        super().__init__()
        self.name = None
        self.type = type_spec

    def personality_action(self, player: Player):
        player.gain_ressource(self.type)
        pass


class Tribune(Personality):
    """
    A class to represent the tribune card

    ...

    Attributes
    ----------

    Methods
    -------
    personality_action()
        function to launch the tribune's actions

    """
    def __init__(self):
        super().__init__()

    def personality_action(self, player: Player):
        # take all card of our discard + return the number of card won
        nb_cards_added = player.discard_pile.__sizeof__()
        for card in player.discard_pile:
            player.hand.append(card)
        money_earned = nb_cards_added - 3
        if money_earned > 0:
            player.gain_money(money_earned)
        player.add_colon()