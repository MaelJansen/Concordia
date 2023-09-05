from abc import ABC, abstractmethod
from Pieces import Resource, Colonist
import Players
from Map import Province, Map
from Map import City, Line, Position
import Cards


class Personality(ABC):
    def __init__(self, p: Players):
        self.name = self.__class__.__name__.replace('_', '')
        self.card_action = None
        self.card_example = None
        self.player: Players = p

    def could_pay_house(self, city: City):
        resource_city: Resource = city.assigned_city_token.assigned_resource

        player_pieces = self.player.my_store_house.my_pieces
        a_brick = False
        a_resource = False
        for piece in player_pieces:
            if piece is Resource:
                if resource_city.name == "brick" and piece.name == "food":
                    return True
                if resource_city.name == piece.name:
                    a_resource = True
                if piece.name == "brick":
                    a_brick = True

        return a_resource and a_brick

    def could_pay(self,*resources):
        for resource in resources:
            if not self.player.my_store_house.my_pieces.contain(resource):
                return False
        return True

    def pay_house(self, city: City):
        good_city: Resource = city.assigned_city_token.assigned_resource
        player_pieces = self.player.my_store_house.my_pieces

        has_pay_good = False
        has_pay_brick = False
        for piece in player_pieces:
            if piece is Resource:
                if good_city.name == "brick" and piece.name == "food":
                    player_pieces.remove(piece)
                    break
                if good_city.name == piece.name and has_pay_good == False:
                    player_pieces.remove(piece)
                    has_pay_good = True
                if piece.name == "brick" and has_pay_brick == False:
                    player_pieces.remove(piece)
                    has_pay_brick = True
            if has_pay_brick and has_pay_good:
                break

    def pay_with_resource(self, *resources):
        for resource in resources:
            self.player.my_store_house.my_pieces.remove(resource)

    def pay_with_resource_by_name(self,*name_resource):
        for resource in self.player.my_store_house.my_pieces:
            if name_resource.__contains__(resource.name):
                self.player.my_store_house.my_pieces.remove(resource)

    @abstractmethod
    def personality_action(self):
        pass


class Architect(Personality):
    """
    A class to represent the architect card

    ...

    Attributes
    ----------

    Methods
    -------
    move_colons()
        function to move a colonist of a player
    personality_action()
        function to launch the architect's actions

    """

    def __init__(self, p: Players):
        super().__init__(p)
        self.card_action = ""

    def move_colons(self):
        while True:
            # Function who could ask the player to choose several of his colonists
            selected_colonist: Colonist = self.player.controller.choose_colonists()
            # Function who could ask the player to choose a way
            selected_line: Line = self.player.controller.choose_way()
            selected_way = selected_line.line_way
            if selected_colonist is None:
                break
            if selected_way is not None:
                colonist = self.player.my_colonist
                colonist.remove(selected_colonist)
                colonist_position: Position = selected_colonist.position
                possible = False
                for city in selected_line.city_list:
                    if colonist_position is City:
                        if city == colonist_position:
                            possible = True
                            break
                    else:
                        if colonist_position.city_list.__contains__(city):
                            possible = True
                            break
                if possible:
                    selected_colonist.colonist_way = selected_way
                    colonist.append(selected_colonist)
                    break

    def personality_action(self):
        self.move_colons()

        # Function who ask the player where we build the house
        while True:
            selected_city: City = self.player.controller.choose_city()
            list_house_player = self.player.house
            if not self.could_pay_house(selected_city):
                break
            if selected_city not in list_house_player:
                list_house_player.append(selected_city)
                self.pay_house(selected_city)
                break


class Colonist_(Personality):
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

    def __init__(self, p: Players):
        super().__init__(p)

    def personality_action(self):
        # We need to ask the player what he wants to do
        choice_add_colon = True
        if choice_add_colon:
            # A function who can demand what colons to add
            self.player.add_colons()
        else:
            self.player.money += 5 + len(self.player.my_colonist)


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

    def __init__(self, p: Players):
        super().__init__(p)

    def personality_action(self):
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

    def __init__(self, p: Players):
        super().__init__(p)

    def personality_action(self):
        # Ask the player to buy a card in market without additional cost
        card_chose: Cards = self.player.buy_in_market(False)
        if card_chose is not None:
            cost_of_card = card_chose.card_cost
            if self.could_pay(cost_of_card):
                self.pay_with_resource(cost_of_card)

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

    def __init__(self, p: Players):
        super().__init__(p)

    def personality_action(self):
        # Ask the player to choice another discard's player
        player_choice: Players = self.player.choice_discard()
        # and play the card on the top of this discard
        discard_player_choice = player_choice.discard_pile
        discard_player_choice[len(discard_player_choice) - 1].my_personality.personality_action(self.player)
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

    def __init__(self, p: Players):
        super().__init__(p)

    def personality_action(self):
        player_finish = False
        if self.was_buy:
            self.player.money += 5
        else:
            self.player.money += 3
        while not player_finish:
            sale = list()
            purchase = list()
            # Ask what the player wants to sell
            sale = self.player.controller.sell()
            # Ask what the player wants to sell
            purchase = self.player.controller.buy()

            for resource in sale:
                resource: Resource
                if self.player.my_store_house.my_pieces.__contain__(resource):
                    self.player.money += resource.price
                    self.player.my_store_house.my_pieces.remove(resource)
            for resource in purchase:
                resource: Resource
                if self.player.money >= resource.price:
                    self.player.money -= resource.price
                    self.player.my_store_house.my_pieces.add(resource)

            player_finish = self.player.controller.finish_deal()


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

    def __init__(self, p: Players):
        super().__init__(p)

    def personality_action(self):
        want_goods = self.player.controller.want_good()
        good_choice = False
        if want_goods:
            while not good_choice:
                province: Province = self.player.controller.choose_province()
                good_choice = province.side_resource_bonus
                if good_choice:
                    self.player.my_store_house.my_pieces.append(province.ressource_bonus)
                    province.side_resource_bonus = False
        else:
            map : Map = self.player.controller.game_map
            for province in map.my_provinces:
                if not province.side_resource_bonus:
                    self.player.money += 1
                    province.side_resource_bonus = True
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

    def __init__(self, p: Players):
        super().__init__(p)

    def personality_action(self):
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

    def __init__(self, p: Players):
        super().__init__(p)

    def personality_action(self):
        card_choose_1: Cards
        card_choose_2: Cards
        card_choose_1, card_choose_2 = self.player.controller.choose_cards_market()
        if card_choose_1 is not None:
            if self.could_pay(card_choose_1.card_cost):
                self.pay_with_resource(card_choose_1.card_cost)
        if card_choose_2 is not None:
            if self.could_pay(card_choose_2.card_cost):
                self.pay_with_resource(card_choose_2.card_cost)
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

    def __init__(self, p: Players, type_spec: Resource):
        super().__init__(p)
        self.type = type_spec

    def personality_action(self):
        for house in self.player.house:
            house: City
            if house.assigned_city_token.ssigned_resource == self.type:
                self.player.my_store_house.my_pieces.append(self.type)
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

    def __init__(self, p: Players):
        super().__init__(p)

    def personality_action(self):
        # take all card of our discard + return the number of card won
        nb_cards_added = self.player.discard_pile.__sizeof__()
        for card in self.player.discard_pile:
            self.player.hand.append(card)
        money_earned = nb_cards_added - 3
        if money_earned > 0:
            self.player.money += money_earned
        selected_colonist: Colonist = self.player.controller.choose_colonist()
        self.player.my_colonist.append(selected_colonist)
