import copy
from abc import ABC, abstractmethod
from Pieces import Resource, Colonist
from Map import City


class Personality(ABC):

    def __init__(self, p: object):
        """ 
        @param p: Player who have the card with this personality
        """
        self.name = self.__class__.__name__.replace('_', '')
        self.card_action = None
        self.card_example = None
        self.player = p

    def could_pay_house(self, city: object):
        """ Find out if you can pay a house in this city

        @param city: the city where you want to pay a house
        @return: True if you can buy a house in this city
        """
        resource_city = city.assigned_city_token.assigned_resource

        player_pieces = self.player.my_store_house.my_pieces
        a_brick = False
        a_resource = False
        for piece in player_pieces:
            if resource_city.name == "brick" and piece.name == "food":
                return True
            if resource_city.name == piece.name:
                a_resource = True
            if piece.name == "brick":
                a_brick = True

        return a_resource and a_brick

    def could_pay(self, *resources):
        """ Find out if you have all resources needed

        @param resources: all resources you need
        @return: true if you have all resources
        """
        if len(resources) == 1:
            resources = resources[0]
        for resource in resources:
            if resource not in self.player.my_store_house.my_pieces:
                return False
        return True

    def pay_house(self, city: City):
        """ Allows you to pay a house

        @param city: the city where you want a house
        """
        good_city: Resource = city.assigned_city_token.assigned_resource
        player_pieces = self.player.my_store_house.my_pieces
        payment_pieces = player_pieces.copy()

        has_pay_good = False
        has_pay_brick = False
        for piece in player_pieces:
            if good_city.name == "brick" and piece.name == "food":
                    payment_pieces.remove(piece)
                    self.player.my_store_house.my_pieces = payment_pieces
                    break
            if good_city.name == piece.name and has_pay_good == False:
                    payment_pieces.remove(piece)
                    has_pay_good = True
            if piece.name == "brick" and has_pay_brick == False:
                    payment_pieces.remove(piece)
                    has_pay_brick = True
            if has_pay_brick and has_pay_good:
                break
        if has_pay_brick and has_pay_good:
            self.player.my_store_house.my_pieces = payment_pieces

    def pay_with_resource(self, *resources):
        """ Allow to pay all resources

        @param resources: all resources to be paid
        """
        if len(resources) == 1:
            resources = resources[0]
        for resource in resources:
            self.player.my_store_house.my_pieces.remove(resource)

    def could_pay_with_name(self,*name_resource):
        """ Check if you can pay all resources

        @param name_resource: all name of resource(s)
        @return: true if you have all there resources
        """
        resources = self.player.my_store_house.my_pieces.copy()
        i = 0
        for resource in resources:
            if resource.name in name_resource:
                i += 1
        return i == len(name_resource)

    def pay_with_resource_by_name(self, *name_resource):
        """ Allow to pay resources by name

        @param name_resource: name(s) of resource(s)
        """
        resources = self.player.my_store_house.my_pieces.copy()
        for resource in resources:
            if resource.name in name_resource:
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

    def __init__(self, p: object):
        super().__init__(p)
        self.card_action = ""

    def move_colons(self):
        """ function to move a colonist of a player

        """
        while True:
            # Function who could ask the player to choose several of his colonists
            selected_colonist = self.game.choose_colonists()
            # Function who could ask the player to choose a way
            selected_line = self.game.controller.choose_way()
            selected_way = selected_line.line_way
            if selected_colonist is None:
                break
            if selected_way is not None:
                colonist = self.player.my_colonist
                colonist.remove(selected_colonist)
                colonist_position = selected_colonist.position
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
        """ function to launch the architect's actions

        """
        self.move_colons()

        # Function who ask the player where we build the house
        while True:
            selected_city: City = self.game.choose_city()
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

    def __init__(self, p: object):
        super().__init__(p)

    def personality_action(self, choice_add_colonist, *colonists: Colonist):
        """ function to launch the colonist's actions

        @param choice_add_colonist: True if the player want to pay a colonist
        @param colonists: all colonist(s) the player want
        """
        # We need to ask the player what he wants to do
        if choice_add_colonist:
            # A function who can demand what colons to add
            for colonist in colonists:
                if self.could_pay_with_name("food","tool"):
                    self.pay_with_resource_by_name("food", "tool")
                    self.player.my_colonist.append(colonist)
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

    def __init__(self, p: object):
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

    def __init__(self, p: object):
        super().__init__(p)

    def personality_action(self, card_choose: object):
        """ function to launch the consul's actions

        @param card_choose: the card of market choose by the player
        """
        if card_choose is not None:
            cost_of_card = card_choose.card_cost
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

    def __init__(self, p: object):
        super().__init__(p)

    def personality_action(self, player_choice: object):
        """ function to launch the diplomat's actions

        @param player_choice: The player of the discard choose by the owner of this card
        """
        # play the card on the top of this discard
        discard_player_choice = player_choice.discard_pile
        discard_player_choice[len(discard_player_choice) - 1].my_personality.personality_action(self.player)


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

    def __init__(self, p: object):
        super().__init__(p)

    def personality_action(self):
        """ function to launch the mercator's action's

        """
        player_finish = False
        if self.was_buy:
            self.player.money += 5
        else:
            self.player.money += 3
        while not player_finish:
            sale = list()
            purchase = list()
            # Ask what the player wants to sell
            sale = self.game.sell()
            # Ask what the player wants to sell
            purchase = self.game.buy()

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

            player_finish = self.game.finish_deal()


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

    def __init__(self, p: object):
        super().__init__(p)

    def personality_action(self):
        """ function to launch the prefect's actions

        """
        had_magnus = False
        prefectus_magnus = None
        for c in self.player.hand:
            if c.my_personality.name == PrefectusMagnus.__name__.replace("_", ""):
                had_magnus = True
                prefectus_magnus = c.my_personality
                break
        want_goods = self.game.want_good()
        good_choice = False
        if want_goods:
            while not good_choice:
                province = self.game.choose_province()
                good_choice = province.side_resource_bonus
                if good_choice:
                    self.player.my_store_house.my_pieces.append(province.ressource_bonus)
                    if had_magnus:
                        self.player.my_store_house.my_pieces.append(province.ressource_bonus)
                        prefectus_magnus.personality_action()
                    province.side_resource_bonus = False
        else:
            map = self.game.game_map
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

    def __init__(self, p: object):
        super().__init__(p)

    def personality_action(self):
        """ function to launch the prefect magnus's actions

        """
        numbers_next_player = ((self.game.current_player_index + 1)
                               % len(self.game.player_list))
        player_next = self.game.player_list[numbers_next_player]
        self.player.hand.remove(self)
        self.player = player_next
        player_next.hand.append(self)
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

    def __init__(self, p: object):
        super().__init__(p)

    def personality_action(self, card_choose_1, card_choose_2, marketplace):
        """ function to launch the senator's actions

        @param card_choose_1: the first card choose by the player for buy it (could be None)
        @param card_choose_2: the second card choose by the player for buy it (could be None)
        @param marketplace: the mark of their card(s)
        """
        if card_choose_1 is not None:
            if self.could_pay(card_choose_1.card_cost):
                self.pay_with_resource(card_choose_1.card_cost)
                self.player.hand.append(card_choose_1)
                marketplace.display_area.remove(card_choose_1)
        if card_choose_2 is not None:
            if self.could_pay(card_choose_2.card_cost):
                self.pay_with_resource(card_choose_2.card_cost)
                self.player.hand.append(card_choose_2)
                marketplace.display_area.remove(card_choose_2)
        pass


class Specialist(Personality):
    """
    A class to represent the specialist card

    ...

    Attributes
    ----------
    type : Resource
        type of resource to which the specialist is linked

    Methods
    -------
    personality_action()
        function to launch the specialist's actions

    """

    def __init__(self, p: object, type_spec: Resource):
        super().__init__(p)
        self.type = type_spec

    def personality_action(self):
        """ function to launch the specialist's actions

        """
        for house in self.player.my_houses:
            house: City
            if house.assigned_city_token.assigned_resource == self.type:
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

    def __init__(self, p: object):
        super().__init__(p)

    def personality_action(self, selected_colonist: object):
        """ function to launch the tribune's actions

        @param selected_colonist: the colonist the player want to pay (could be None)
        """
        # take all card of our discard + return the number of card won
        nb_cards_added = len(self.player.discard_pile) + 1
        save = copy.copy(self.player.discard_pile)
        for card in self.player.discard_pile:
            self.player.hand.append(card)
            self.player.discard_pile.remove(card)
        money_earned = nb_cards_added - 3
        if money_earned > 0:
            self.player.money += money_earned
        if selected_colonist is not None and self.could_pay_with_name("food","tool"):
            self.player.my_colonist.append(selected_colonist)
            self.pay_with_resource_by_name("food", "tool")
