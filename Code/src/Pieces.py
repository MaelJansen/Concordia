from abc import ABC, abstractmethod
import Map
import typing


class Piece(ABC):
    """
    A class to represent the piece (resource and colonist)

    ...

    Attributes
    ----------

    Methods
    -------

    """

    def __init__(self):
        pass


class Colonist(Piece):
    """
    A class to represent colonists in the game Concordia.

    Attributes
    ----------
    type : str
        The type of colonist.
    color : str
        The color associated with the colonist.
    colonist_way : Way
        The way or path that the colonist follows.

    Methods
    -------
    move(self, way)
        Move the colonist along the specified way.

    """

    def __init__(self, colonist_type, colonist_color):
        super().__init__()
        self.type = colonist_type
        self.color = colonist_color
        self.colonist_way = None

    def move(self, way):
        if way.is_valid_move_for_colonist(self):
            self.colonist_way = way
            way.occupant = self
            print(f"{self.color} colonist moved along {way.name}.")
        else:
            print("Invalid move for the colonist.")

    def __repr__(self) -> str:
        return f"{self.color} {self.type} colonist"


class ResourceType:
    """
    A class to represent resources in the game Concordia.

    Attributes
    ----------
    price : int
        The price of the resource.
    bonus_value : int
        A bonus value associated with the resource.
    type : str
        The type of the resource (e.g., "brick", "food", "tool", "wine", "cloth").
    build_cost : int
        The cost of building or producing the resource.
    color : str
        The color associated with the resource.

    Methods
    -------
    __init__(self, resource_price, resource_bonus_value, build_cost, resource_color)
        Initializes a new instance of the Resource class.
    get_info(self)
        Returns a string with information about the resource.

    """
    # static
    RESOURCE_TYPES: typing.Dict[str, object] = {}

    def __init__(self, name: typing.Text, resource_price, resource_bonus_value, build_cost, resource_color):
        self.name = name
        self.price = resource_price
        self.bonus_value = resource_bonus_value
        self.build_cost = build_cost
        self.color = resource_color

    def get_info(self):
        info = f"Name: {self.name}\n"
        info += f"Color: {self.color}\n"
        info += f"Bonus Value: {self.bonus_value}\n"
        info += f"Price: {self.price}\n"
        info += f"Build Cost: {self.build_cost}\n"
        return info

    def setup_resource_types(data):
        for r_t in data:
            resource_name, resource_price, resource_color, resource_bonus_value, build_cost = r_t[0], r_t[1], r_t[2], \
            r_t[3], r_t[4]
            res_type_obj = ResourceType(resource_name, resource_price, resource_bonus_value, build_cost, resource_color)
            ResourceType.RESOURCE_TYPES[resource_name] = res_type_obj


class Resource(Piece):
    def __init__(self, res_type: typing.Type[ResourceType]):
        self.resource_type = res_type

    def __repr__(self) -> str:
        return f"{self.resource_type.name} resource"
