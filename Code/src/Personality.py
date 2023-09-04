from abc import ABC, abstractmethod
from Piece import Ressource


class Personality(ABC):"""
    A class to represent the personality of cards and their actions

    ...

    Attributes
    ----------
    name : sting
    card_action : srting
    card_example : string

    Methods
    -------
    personality_action()
        the action that will be launch when we play the card
    """
    def __init__(self):
        self.name = self.__class__.__name__.replace('_', '')
        self.card_action = None
        self.card_example = None

    def personality_action():
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

    @abstractmethod
    def personality_action():
        pass

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
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

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

    @abstractmethod
    def personality_action():
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

    @abstractmethod
    def personality_action():
        pass

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

    @abstractmethod
    def personality_action():
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
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

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

    @abstractmethod
    def personality_action():
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

    @abstractmethod
    def personality_action():
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

    @abstractmethod
    def personality_action():
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
    def __init__(self):
        super().__init__()
        self.name = None

    @abstractmethod
    def personality_action():
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

    @abstractmethod
    def personality_action():
        pass