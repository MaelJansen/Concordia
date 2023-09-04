from ast import List, Tuple
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from screeninfo import get_monitors
from Player import Player
from Map import Map
import typing

class GameManager:
    """
    A class to control the game 

    ...

    Attributes
    ----------
    player_controller : PlayerManager
    game_map : Map
    player_list : List<Player>
    player_color : List<Tuple()>

    Methods
    -------
    initialization_script()
        The method to setup the game

    """
    def __init__(self):
        self.player_controller = None
        self.game_map = None
        self.player_list = ()
        self.initialization_script()

    def initialization_script(self):
        self.createInterface()

    def createInterface(self):
        root = tk.Tk()
        concordia_screen = Screen(root)
        root.mainloop()  # Démarrer la boucle principale de l'interface graphique

class PlayerController:
    pass

class Screen:
    def __init__(self, root: tk.Tk):
        self.root: tk.Tk = root
        self.player_number: int = 0
        self.ai_number: int = 0
        self.ai_difficulty: str = ""
        self.game_map: str = ""
        self.imperium_button: tk.Button 
        self.italy_button: tk.Button 
        self.createMenuUI()

    def createMenuUI(self):
        self.root.title("Concordia")
        dimensions: Tuple[int, int] = get_monitors()[0]
        self.root.geometry(f"{dimensions.width}x{dimensions.height}")

        # Reset du nombre de joueurs en cas de partie terminée
        self.player_number = None
        self.ai_number = None
        self.ai_difficulty = None
        self.game_map = None

        # Charger l'image
        image: Image.Image = Image.open("Code/src/Images/fond.png")
        image = image.resize((dimensions.width, dimensions.height), Image.LANCZOS) 
        self.photo = ImageTk.PhotoImage(image)

        # Créer un label pour afficher l'image
        label:tk.Label = tk.Label(self.root, image=self.photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Placement des boutons
        self.imperium_button = tk.Button(self.root, text="Imperium", command=lambda: self.player_configuration("Imperium", 5), font=("Helvetica", 24))
        self.imperium_button.place(x=dimensions.width // 2 - 150, y=dimensions.height // 2 - 60, width=300, height=120)
        self.italy_button = tk.Button(self.root, text="Italy", command=lambda: self.player_configuration("Italie", 4), font=("Helvetica", 24))
        self.italy_button.place(x=dimensions.width // 2 - 150, y=dimensions.height // 2 + 100, width=300, height=120)


    def player_configuration(self, name: str, max_players: int):
        self.game_map = name

        self.imperium_button.configure(state="disabled")
        self.italy_button.configure(state="disabled")

        windows:tk.Toplevel = tk.Toplevel(self.root)
        windows.title(f"{name} configuration")
        windows.resizable(False, False)

        windows_width:int = 300
        windows_height:int = 110

        dimensions: Tuple[int, int] = get_monitors()[0]

        x_coordinate:int = int((dimensions.width - windows_width) // 2)
        y_coordinate:int = int((dimensions.height - windows_height) // 2)

        windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

        player_number_label:tk.Label = tk.Label(windows, text="Choose the number of players :")
        player_number_label.pack()

        player_number_box:ttk.Combobox = ttk.Combobox(windows, values=[str(i) for i in range(max_players + 1)])
        player_number_box.set("0")
        player_number_box.pack(padx=20, pady=10)

        bouton:tk.Button = tk.Button(windows, text="Validate", command=lambda: self.ai_configuration(player_number_box.get(), max_players, windows))
        bouton.pack(pady=10)

        windows.protocol("WM_DELETE_WINDOW", lambda: self.on_screen_close(windows))

    def ai_configuration(self, player_number: str, max_players: int, windows: tk.Toplevel):
        self.player_number = int(player_number)
        if self.player_number != max_players:
            windows.destroy()
            self.imperium_button.configure(state="disabled")
            self.italy_button.configure(state="disabled")

            self.player_number = int(player_number)

            max_ia: int = max_players - self.player_number

            if self.player_number == 0:
                min_ia: int = 2
            elif self.player_number == 1:
                min_ia: int = 1
            else:
                min_ia: int = 0

            values: List[str] = [str(i) for i in range(min_ia, max_ia + 1)]

            windows: tk.Toplevel = tk.Toplevel(self.root)
            windows.title("Imperium configuration")
            windows.resizable(False, False)

            windows_width: int = 300
            windows_height: int = 110

            dimensions: Tuple[int, int] = get_monitors()[0]

            x_coordinate: int = (dimensions.width - windows_width) // 2
            y_coordinate: int = (dimensions.height - windows_height) // 2

            windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

            ai_number_label: tk.Label = tk.Label(windows, text="Choose the number of AI :")
            ai_number_label.pack()

            ai_number_box: ttk.Combobox = ttk.Combobox(windows, values=values)
            if self.player_number > 1:
                ai_number_box.set("0")
            elif self.player_number == 1:
                ai_number_box.set("1")
            else:
                ai_number_box.set("2")
            ai_number_box.pack(padx=20, pady=10)

            bouton: tk.Button = tk.Button(windows, text="Validate", command=lambda: self.ai_difficulty_configuration(ai_number_box.get(), windows))
            bouton.pack(pady=10)

            windows.protocol("WM_DELETE_WINDOW", lambda: self.on_screen_close(windows))
        else:
            self.game_screen(None, windows)

    def ai_difficulty_configuration(self, ai_number: str, windows: tk.Toplevel):
        self.ai_number = int(ai_number)
        if(self.ai_number != 0):
            windows.destroy()
            self.imperium_button.configure(state="disabled")
            self.italy_button.configure(state="disabled")

            windows: tk.Toplevel = tk.Toplevel(self.root)
            windows.title("AI difficulty configuration")
            windows.resizable(False, False)

            windows_width: int = 300
            windows_height: int = 110

            dimensions: Tuple[int, int] = get_monitors()[0]

            x_coordinate: int = int((dimensions.width - windows_width) // 2)
            y_coordinate: int = int((dimensions.height - windows_height) // 2)

            windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

            ai_difficulty_label:tk.Label = tk.Label(windows, text="Choose the AI difficuly :")
            ai_difficulty_label.pack()

            ai_difficulty_box: ttk.Combobox = ttk.Combobox(windows, values=["Esay", "Medium", "Difficult"])
            ai_difficulty_box.set("Medium")
            ai_difficulty_box.pack(padx=20, pady=10)

            bouton: tk.Button = tk.Button(windows, text="Validate", command=lambda: self.game_screen(ai_difficulty_box.get(), windows))
            bouton.pack(pady=10)

            windows.protocol("WM_DELETE_WINDOW", lambda: self.on_screen_close(windows))
        else:
            self.game_screen(None, windows)

    def on_screen_close(self, windows: tk.Toplevel):
        windows.destroy()
        self.imperium_button.configure(state="normal")
        self.italy_button.configure(state="normal")
        windows.destroy()

    def game_screen(self, ai_difficulty: str, windows: tk.Toplevel):
        windows.destroy()
        if(self.ai_number != 0):
            self.ai_difficulty = ai_difficulty

        self.root.title("Concordia")
        dimensions: Tuple[int, int] = get_monitors()[0]
        self.root.geometry(f"{dimensions.width}x{dimensions.height}")

        temp_label: tk.Label = tk.Label(self.root, text="Cette écran n'est pour la moment pas programmé " + self.game_map + ", il y a " + str(self.player_number) + " joueurs et " + str(self.ai_number) + " IA.")
        temp_label.pack()
        
if __name__ == "__main__":
    game_controller = GameController()
