from abc import ABC, abstractmethod
from ast import List, Tuple
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from screeninfo import get_monitors
from Player import Player
from Map import Map
import typing
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
        name: str = 'Colonist'
        card_action: str = 'You may place a colonist on a city tile that does not have a colonist.'
    
    @abstractmethod
    def personality_action(player: Player):
        windows = tk.Toplevel(root)
        windows.title("Configuration de l'action")
        windows.resizable(False, False)

        # Dimensions de la fenêtre
        windows_width = 300
        windows_height = 110

        # Récupération des dimensions de l'écran
        dimensions = get_monitors()[0]

        x_coordinate = int((dimensions.width - windows_width) // 2)
        y_coordinate = int((dimensions.height - windows_height) // 2)

        windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

        action_label = tk.Label(windows, text="Choisissez une action:")
        action_label.pack()

        def place_colons():
            action_result_label.config(text="Vous avez choisi de placer des colons.")
            
            colon_count = player.my_colonists.count
            wheat_needed = colon_count 
            tool_needed = colon_count  

            if wheat_needed <= player_wheat_count and tool_needed <= player_tool_count:
                player_wheat_count -= wheat_needed
                player_tool_count -= tool_needed

        def collect_sesterces():
            action_result_label.config(text="Vous avez choisi de récupérer des sesterces.")

        place_colons_button = tk.Button(windows, text="Placer des colons", command=place_colons)
        place_colons_button.pack()

        collect_sesterces_button = tk.Button(windows, text="Récupérer des sesterces", command=collect_sesterces)
        collect_sesterces_button.pack()

        action_result_label = tk.Label(windows, text="")
        action_result_label.pack()

        windows.mainloop()
            

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