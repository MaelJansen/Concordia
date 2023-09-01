import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from screeninfo import get_monitors
import os
from Player import Player
from Map import Map

class GameController:
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
    def __init__(self, root):
        self.root = root
        self.player_number = None
        self.ai_number = None
        self.ai_difficulty = None
        self.game_map = None
        self.imperium_button = None
        self.italy_button = None
        self.createMenuUI()

    def createMenuUI(self):
        self.root.title("Concordia")
        dimensions = get_monitors()[0]
        self.root.geometry(f"{dimensions.width}x{dimensions.height}")

        # Reset du nombre de joueurs en cas de partie terminé 
        self.player_number = None
        self.ai_number = None
        self.ai_difficulty = None
        self.game_map = None

        # Charger l'image
        image = Image.open("Code/src/Images/fond.png")
        image = image.resize((dimensions.width, dimensions.height), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)

        # Créer un label pour afficher l'image
        label = tk.Label(self.root, image=self.photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
                
        # Placement des bouttons
        self.imperium_button = tk.Button(self.root, text="Imperium", command=self.imperium_player_configuration, font=("Helvetica", 24))
        self.imperium_button.place(x=dimensions.width//2 + 50, y=dimensions.height//2 -60, width=300, height=120)
        self.italy_button = tk.Button(self.root, text="Italy", command=self.italy_player_configuration, font=("Helvetica", 24))
        self.italy_button.place(x=dimensions.width//2 - 375, y=dimensions.height//2 - 60, width=300, height=120)

    def imperium_player_configuration(self):
        self.game_map = "Imperium"

        self.imperium_button.configure(state="disabled")
        self.italy_button.configure(state="disabled")
        
        imperium_windows = tk.Toplevel(self.root)
        imperium_windows.title("Imperium configuration")
        imperium_windows.resizable(False, False)

        windows_width = 300
        windows_height = 110

        dimensions = get_monitors()[0]

        x_coordinate = (dimensions.width - windows_width) // 2
        y_coordinate = (dimensions.height - windows_height) // 2

        imperium_windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

        player_number_label = tk.Label(imperium_windows, text="Choose the number of players :")
        player_number_label.pack()

        player_number_box = ttk.Combobox(imperium_windows, values=["0", "1", "2", "3", "4", "5"])
        player_number_box.set("0")
        player_number_box.pack(padx=20, pady=10)

        bouton = tk.Button(imperium_windows, text="Validate", command=lambda: self.imperium_AI_configuration(player_number_box.get(), imperium_windows))
        bouton.pack(pady=10)

        imperium_windows.protocol("WM_DELETE_WINDOW", lambda: self.on_screen_close(imperium_windows))

    def imperium_AI_configuration(self, player_number, imperium_windows):
        self.player_number = int(player_number)
        if(self.player_number != 5):
            imperium_windows.destroy()
            self.imperium_button.configure(state="disabled")
            self.italy_button.configure(state="disabled")

            if self.player_number == 0:
                values=["2", "3", "4", "5"]
            elif self.player_number == 1:
                values=["1", "2", "3", "4"]
            elif self.player_number == 2:
                values=["0", "1", "2", "3"]
            elif self.player_number == 3:
                values=["0", "1", "2"]
            elif self.player_number == 4:
                values=["0", "1"]

            imperium_windows = tk.Toplevel(self.root)
            imperium_windows.title("Imperium configuration")
            imperium_windows.resizable(False, False)

            windows_width = 300
            windows_height = 110

            dimensions = get_monitors()[0]

            x_coordinate = (dimensions.width - windows_width) // 2
            y_coordinate = (dimensions.height - windows_height) // 2

            imperium_windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

            ai_number_label = tk.Label(imperium_windows, text="Choose the number of AI :")
            ai_number_label.pack()

            ai_number_box = ttk.Combobox(imperium_windows, values = values)
            if(self.player_number > 1):
                ai_number_box.set("0")
            elif(self.player_number == 1):
                ai_number_box.set("1")
            else:
                ai_number_box.set("2")
            ai_number_box.pack(padx=20, pady=10)

            bouton = tk.Button(imperium_windows, text="Validate", command=lambda: self.ai_difficulty_configuration(ai_number_box.get(), imperium_windows))
            bouton.pack(pady=10)

            imperium_windows.protocol("WM_DELETE_WINDOW", lambda: self.on_screen_close(imperium_windows))
        else:
            self.game_screen("0", None, imperium_windows)

    def italy_player_configuration(self):
        self.game_map = "Italy"

        self.imperium_button.configure(state="disabled")
        self.italy_button.configure(state="disabled")

        italy_windows = tk.Toplevel(self.root)
        italy_windows.title("Italy configuration")
        italy_windows.resizable(False, False)

        player_number_label = tk.Label(italy_windows, text="Choose the number of players :")
        player_number_label.pack()

        windows_width = 300
        windows_height = 110

        dimensions = get_monitors()[0]

        x_coordinate = (dimensions.width - windows_width) // 2
        y_coordinate = (dimensions.height - windows_height) // 2

        italy_windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

        player_number_box = ttk.Combobox(italy_windows, values=["0", "1", "2", "3", "4"])
        player_number_box.set("0")
        player_number_box.pack(padx=20, pady=10)

        bouton = tk.Button(italy_windows, text="Validate", command=lambda: self.italy_ai_configuration(player_number_box.get(), italy_windows))
        bouton.pack(pady=10)

        italy_windows.protocol("WM_DELETE_WINDOW", lambda: self.on_screen_close(italy_windows))

    def italy_ai_configuration(self, player_number, italy_windows):
        self.player_number = int(player_number)
        if self.player_number != 5:
            italy_windows.destroy()
            self.imperium_button.configure(state="disabled")
            self.italy_button.configure(state="disabled")

            
            if self.player_number != 4:
                if self.player_number == 0:
                    values=["2", "3", "4"]
                elif self.player_number == 1:
                    values=["1", "2", "3"]
                elif self.player_number == 2:
                    values=["0", "1", "2"]
                elif self.player_number == 3:
                    values=["0", "1"]

            italy_windows = tk.Toplevel(self.root)
            italy_windows.title("Imperium configuration")
            italy_windows.resizable(False, False)

            windows_width = 300
            windows_height = 110

            dimensions = get_monitors()[0]

            x_coordinate = (dimensions.width - windows_width) // 2
            y_coordinate = (dimensions.height - windows_height) // 2

            italy_windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

            ai_number_label = tk.Label(italy_windows, text="Choose the number of AI :")
            ai_number_label.pack()

            ai_number_box = ttk.Combobox(italy_windows, values = values)
            if(self.player_number > 1):
                ai_number_box.set("0")
            elif(self.player_number == 1):
                ai_number_box.set("1")
            else:
                ai_number_box.set("2")
            ai_number_box.pack(padx=20, pady=10)

            bouton = tk.Button(italy_windows, text="Validate", command=lambda: self.ai_difficulty_configuration(ai_number_box.get(), italy_windows))
            bouton.pack(pady=10)

            italy_windows.protocol("WM_DELETE_WINDOW", lambda: self.on_screen_close(italy_windows))
        else:
            self.game_screen("0", None, italy_windows)

    def ai_difficulty_configuration(self, ai_number, windows):
        self.ai_number = int(ai_number)
        if(self.ai_number != 0):
            windows.destroy()
            self.imperium_button.configure(state="disabled")
            self.italy_button.configure(state="disabled")

            windows = tk.Toplevel(self.root)
            windows.title("AI difficulty configuration")
            windows.resizable(False, False)

            windows_width = 300
            windows_height = 110

            dimensions = get_monitors()[0]

            x_coordinate = (dimensions.width - windows_width) // 2
            y_coordinate = (dimensions.height - windows_height) // 2

            windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

            ai_difficulty_label = tk.Label(windows, text="Choose the AI difficuly :")
            ai_difficulty_label.pack()

            ai_difficulty_box = ttk.Combobox(windows, values=["Esay", "Medium", "Difficult"])
            ai_difficulty_box.set("Medium")
            ai_difficulty_box.pack(padx=20, pady=10)

            bouton = tk.Button(windows, text="Validate", command=lambda: self.game_screen(ai_difficulty_box.get(), windows))
            bouton.pack(pady=10)

            windows.protocol("WM_DELETE_WINDOW", lambda: self.on_screen_close(windows))
        else:
            self.game_screen(None, windows)

    def on_screen_close(self, windows):
        windows.destroy()
        self.imperium_button.configure(state="normal")
        self.italy_button.configure(state="normal")
        windows.destroy()

    def game_screen(self, ai_difficulty, windows):
        windows.destroy()
        if(self.ai_number != 0):
            self.ai_difficulty = ai_difficulty

        self.root.title("Concordia")
        dimensions = get_monitors()[0]
        self.root.geometry(f"{dimensions.width}x{dimensions.height}")

        temp_label = tk.Label(self.root, text="Cette écran n'est pour la moment pas programmé " + self.game_map + ", il y a " + str(self.player_number) + " joueurs et " + str(self.ai_number) + " IA.")
        temp_label.pack()
        
if __name__ == "__main__":
    game_controller = GameController()
