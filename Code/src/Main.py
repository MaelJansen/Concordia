from ast import List, Set, Tuple
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from screeninfo import get_monitors
from Player import Player
from Map import Map
from typing import Type

class GameManager:
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
        root.mainloop() 

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
        self.temp_capitale: Tuple[str, int, int]
        self.temp_villes: List[Tuple[str, int, int]]
        self.temp_routes: Set[Tuple[Tuple[str, int, int], Tuple[str, int, int], str]]

        self.create_game()

    def temp_game(self):
        self.temp_capitale = ("Rome", 500, 500)
        self.temp_villes = [("Venise", 100, 100), ("Paris", 50, 60), ("Madrid", 456, 689), ("Berlin", 870, 900), ("Tokyo", 321, 457), ("Sao-Paulo", 132, 873), ("Sao-Carlos", 103, 832), ("Biganos", 578, 213), ("Prague", 643, 43)]
        self.temp_routes = [(self.temp_villes[5], self.temp_villes[6], "Land"), (self.temp_villes[5], self.temp_villes[6], "Water"), (self.temp_villes[5], self.temp_villes[6], "Air"), (self.temp_villes[5], self.temp_villes[2], "Land"), (self.temp_villes[2], self.temp_capitale, "Water"), (self.temp_villes[2], self.temp_villes[6], "Air")]


    def create_game(self):
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
        if self.ai_number != 0:
            self.ai_difficulty = ai_difficulty

        self.root.title("Concordia")
        dimensions: Tuple[int, int] = get_monitors()[0]
        self.root.geometry(f"{dimensions.width}x{dimensions.height}")

        canvas:tk.Canvas = tk.Canvas(self.root, width=dimensions.width, height=dimensions.height)
        canvas.pack()

        border_width:int = 20
        canvas.create_rectangle(0, 0, self.root.winfo_screenwidth(), self.root.winfo_screenheight(), outline="black", width=border_width)
        canvas.create_rectangle(border_width, border_width, self.root.winfo_screenwidth() - border_width, self.root.winfo_screenheight() - border_width, fill="white")
        canvas.create_line(border_width, dimensions.height*0.25, dimensions.width - border_width, dimensions.height*0.25, fill="black", width=3) 
        canvas.create_line(dimensions.width * 0.33, border_width, dimensions.width * 0.33, dimensions.height*0.25, fill="black", width=3) 

        self.temp_game()

        max_x:int = 0
        max_y:int = 0

        for ville in self.temp_villes:
            nom, x, y = ville
            max_x = max(max_x, x)  
            max_y = max(max_y, y) 

        coeff_difference_x:float = (dimensions.width - border_width * 4) / max_x
        coeff_difference_y:float = (dimensions.height * 0.75 - border_width * 4) / max_y

        canvas.create_oval((self.temp_capitale[1] * coeff_difference_x) + border_width - 10, (self.temp_capitale[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) - 10, (self.temp_capitale[1] * coeff_difference_x) + border_width + 10, (self.temp_capitale[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) + 10, fill="red")
        canvas.create_text((self.temp_capitale[1] * coeff_difference_x) + border_width, (self.temp_capitale[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) + 15, text=self.temp_capitale[0], font=("Helvetica", 8))

        for cities in self.temp_villes:
            canvas.create_oval((cities[1] * coeff_difference_x) + border_width - 10, (cities[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) - 10, (cities[1] * coeff_difference_x) + border_width + 10, (cities[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) + 10, fill="black")
            canvas.create_text((cities[1] * coeff_difference_x) + border_width, (cities[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) + 15, text=cities[0], font=("Helvetica", 8))

        for way in self.temp_routes:
            x_coordinate, y_coordinate, transport_mode = way

            if(transport_mode == "Land"):
                color:str = "lightgreen"
            elif(transport_mode == "Water"):
                color:str = "blue"
            else:
                color:str = "gray"

            canvas.create_line((x_coordinate[1] * coeff_difference_x) + border_width, (y_coordinate[1] * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3), (x_coordinate[2] * coeff_difference_x) + border_width, (y_coordinate[2] * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3), fill=color, width=2)
        
if __name__ == "__main__":
    game_controller = GameManager()
