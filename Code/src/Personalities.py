from abc import ABC, abstractmethod
from ast import List, Tuple
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from screeninfo import get_monitors
import Map
import typing
import Pieces


class Personality(ABC):
    """
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
        name: str = 'Architect'
        card_action: str = 'You may build a city tile for free and move your colonists to it.'

    @abstractmethod
    def personality_action():
        windows = tk.Toplevel(root)
        windows.title("Move your colonists")
        windows.resizable(False, False)

        windows_width = 300
        windows_height = 110

        dimensions = get_monitors()[0]

        x_coordinate = int((dimensions.width - windows_width) // 2)
        y_coordinate = int((dimensions.height - windows_height) // 2)

        windows.geometry(
            f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")


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
        name: str = 'Colonist'
        card_action: str = 'You may place a colonist on a city tile that does not have a colonist.'

    @abstractmethod
    def personality_action(player: object, root: tk.Tk, map: Map):
        """"
        Play the personality action of the player

        Args:
            player (Player): The player who is playing
            root (tk.Tk): The main window
            map (Map): The map of the game

        Returns:
            None

        """
        windows = tk.Toplevel(root)
        windows.title("Configuration de l'action")
        windows.resizable(False, False)

        windows_width = 300
        windows_height = 110

        dimensions = get_monitors()[0]

        x_coordinate = int((dimensions.width - windows_width) // 2)
        y_coordinate = int((dimensions.height - windows_height) // 2)

        windows.geometry(
            f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

        action_label = tk.Label(windows, text="Choose an action:")
        action_label.pack()

        def place_colons():
            action_result_label.config(
                text="You have chosen to place colonists.")

            colon_count = player.my_colonists.count
            wheat_needed = colon_count
            tool_needed = colon_count

            if player.my_store_house.my_ressources[0].count < wheat_needed or player.my_store_house.my_ressources[1].count < tool_needed:
                action_result_label.config(
                    text="You don't have enough ressources.")
                return

            player.my_store_house.my_ressources[0].count -= wheat_needed
            player.my_store_house.my_ressources[1].count -= tool_needed
            player.my_colonists.count += colon_count

            city_tile_window = tk.Toplevel(root)
            city_tile_window.title("Choose a city to place your colonists.")
            city_tile_window.resizable(False, False)

            city_tile_window_width = 300
            city_tile_window_height = 110

            dimensions = get_monitors()[0]

            x_coordinate = int(
                (dimensions.width - city_tile_window_width) // 2)
            y_coordinate = int(
                (dimensions.height - city_tile_window_height) // 2)

            city_tile_window.geometry(
                f"{city_tile_window_width}x{city_tile_window_height}+{x_coordinate}+{y_coordinate}")

            city_tile_label = tk.Label(
                city_tile_window, text="Choose a city tile:")
            city_tile_label.pack()

            city_tile_box = ttk.Combobox(
                city_tile_window, values=map.city_tiles)
            city_tile_box.pack()

            new_colon: Pieces.Colonist = Pieces.Colonist()
            new_colon.move(map.city_tiles[city_tile_box.current()])

        def collect_sesterces():
            action_result_label.config(
                text="Vous avez choisi de récupérer des sesterces.")

            player.money += player.my_colonists.count + 5

        place_colons_button = tk.Button(
            windows, text="Placer des colons", command=place_colons)
        place_colons_button.pack()

        collect_sesterces_button = tk.Button(
            windows, text="Récupérer des sesterces", command=collect_sesterces)
        collect_sesterces_button.pack()

        action_result_label = tk.Label(windows, text="")
        action_result_label.pack()

        windows.mainloop()


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
