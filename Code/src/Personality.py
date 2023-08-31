from abc import ABC, abstractmethod
from Piece import Ressource

class Personality(ABC):
    def __init__(self):
        self.name = self.__class__.__name__.replace('_', '')
        self.card_action = None
        self.card_example = None

    def personality_action():
        pass

class Architect(Personality):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

class Colonist_(Personality):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

class Concordia(Personality):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

class Consul(Personality):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

class Diplomat(Personality):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

class Mercator(Personality):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

class Prefect(Personality):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

class PrefectusMagnus(Personality):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass


class Senator(Personality):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

class Specialist(Personality):
    def __init__(self):
        super().__init__()
        self.name = None

    @abstractmethod
    def personality_action():
        pass

class Tribune(Personality):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass

class Concordia(Personality):
    def ___init___(self):
        super().__init__()

    @abstractmethod
    def personality_action():
        pass