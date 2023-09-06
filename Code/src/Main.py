from ast import List, Set, Tuple
from math import atan2, degrees
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from screeninfo import get_monitors
#import Players
import Map
from typing import Type
import oracledb

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
        self.player_list = []  
        self.current_player_index = 0  # Index of the current player
        self.connection = oracledb.connect(
            user="ETD",
            password="ETD",
            host="info-atchoum.iut.bx",
            port=1521,
            sid="IUT12c"
        )
        self.cursor = self.connection.cursor()
        
        self.get_player_setup_data()

    def initialization_script(self):
        self.createInterface()

    def createInterface(self):
        root = tk.Tk()
        concordia_screen = Screen(root)
        root.mainloop() 

    def start_game(self):
        # Initialize the game, set up the map, create players, etc.
        self.game_map = Map()  # Replace with actual map initialization
        self.create_players()  # Create players here
        self.setup_players()

        # Start the first player's turn
        self.start_next_player_turn()

    def create_players(self):
        num_players = len(self.player_list)
        if num_players < 2:
            print("At least two players are required to start the game.")
            return

        for player_num in range(num_players):
            player_name = f"Player {player_num + 1}"
            self.player_list.append(Players.Player(player_name))  # Replace with actual player creation

    def setup_players(self):
        # Use SQL queries to get player setup data here
        player_setup_data = self.get_player_setup_data()

        # Assign player setup data to each player
        for player_num, setup_data in enumerate(player_setup_data):
            current_player = self.player_list[player_num]

            # Extract colonists setup data
            colonist_data = setup_data.get("colonists", {})
            current_player.setup_colonists(colonist_data)

            # Extract goods setup data
            goods_data = setup_data.get("goods", {})
            current_player.setup_goods(goods_data)

            # Extract houses setup data
            houses_data = setup_data.get("houses", 0)
            current_player.setup_houses(houses_data)

            # Extract player setup cards data
            cards_data = setup_data.get("cards", {})
            current_player.setup_cards(cards_data)

            # Extract sestertii setup data
            sestertii_data = setup_data.get("sestertii", {})
            current_player.setup_sestertii(sestertii_data)

    def get_player_setup_data(self):
        # Implement SQL queries to retrieve player setup data
        # Execute the SQL queries and retrieve the data
        sql_query_colonists = f"""SELECT spc.setup_p_colon_way,
                            spc.setup_p_colon_n_colonists,
                            spc.setup_p_colon_n_colonists_cap
                            FROM T_Concordia t, table(t.concordia_setup_player.setup_p_colonist) spc"""
        
        self.cursor.execute(sql_query_colonists)
        colonists_data=[]
        for row in self.cursor:
            temp_colonists_data = [row[0], row[1], row[2]]
            colonists_data.append(temp_colonists_data)
        
        print(colonists_data)

        sql_query_goods = f"""SELECT spg.setup_p_good_good ,
                            spg.setup_p_good_n_goods
                            FROM T_Concordia t, table(t.concordia_setup_player.setup_p_good) spg"""
        
        self.cursor.execute(sql_query_goods)
        goods_data=[]
        for row in self.cursor:
            temp_goods_data = [row[0], row[1]]
            goods_data.append(temp_goods_data)
        
        print(goods_data)

        sql_query_cards = f"""SELECT spc.setup_p_card_card ,
                            spc.setup_p_card_n_copies
                            FROM T_Concordia t, table(t.concordia_setup_player.setup_p_card) spc """
        

        # Example data (replace with actual data)
        player_setup_data = [
            {
                "colonists": {"way": "some_way", "n_colonists": 5, "n_colonists_cap": 10},
                "goods": {"good": "some_good", "n_goods": 20},
                "houses": 3,
                "cards": {"card": "some_card", "n_copies": 2},
                "sestertii": {"order_of_play": 1, "n_sestertii": 50, "n_sestertii_variant": 100},
            },
            # Add data for other players here
        ]

        return player_setup_data

    def start_next_player_turn(self):
        # Get the current player
        current_player = self.player_list[self.current_player_index]

        # Start the player's turn (you need to implement this in PlayerController)
        self.player_controller.start_player_turn(current_player)

        # Increment the current player index
        self.current_player_index = (self.current_player_index + 1) % len(self.player_list)

    def end_game(self):
        # End the game, calculate scores, display results, etc.
        pass
   
class PlayerController:
    pass

class Screen:
    """This class create the display of the game (main menu, gameplay...)
    """
    def __init__(self, root: tk.Tk):
        """Initialize an instance of the screen class.

        Args:
        root (tk.Tk): An instance of the main application window.
        """
        self.root: tk.Tk = root
        self.player_number: int = 0
        self.ai_number: int = 0
        self.ai_difficulty: str = ""
        self.game_map: str = ""
        self.maps: list[str] = []
        self.map_button: List[tk.Button]
        self.capital: Tuple[str, int, int]
        self.cities: List[Tuple[str, int, int]] = []
        self.roads: Set[Tuple[Tuple[str, int, int], Tuple[str, int, int], str]] = []

        self.create_game()
        

    def charge_map(self):
        """This method uses SQL resquests to get the capital, the cities and the ways of the map that have been choosed by the player to place them in list. The lists
        will be used to display the city, ways... on the map. 
        """
        sql_query_capital = f"""SELECT t.MAP_CAPITAL.CITY_NAME AS CAPITAL, t.MAP_CAPITAL.CITY_COORDINATES.X as x, t.MAP_CAPITAL.CITY_COORDINATES.Y as y
                            FROM T_Concordia, TABLE(T_Concordia.concordia_map) t 
                            WHERE t.map_name='{self.game_map}'"""
        self.cursor.execute(sql_query_capital)
        for row in self.cursor:
            self.capital = [row[0], row[1], row[2]]
            
            
        sql_query_cities = f"""SELECT c.CITY_NAME as city_name,
                            c.CITY_COORDINATES.X as x,
                            c.CITY_COORDINATES.Y as y
                            FROM T_Concordia, TABLE(T_Concordia.concordia_map) t , TABLE(t.MAP_PROVINCE) p , TABLE(p.province_city) c
                            WHERE t.map_name='{self.game_map}'"""
        self.cursor.execute(sql_query_cities)
        for city in self.cursor:
            temp_city = [city[0], city[1], city[2]]
            self.cities.append(temp_city)
            
        sql_query_lines = f"""SELECT l.line_city_1 city1, l.line_city_2 city2, l.line_way way
                            FROM T_Concordia, TABLE(T_Concordia.concordia_map) t, TABLE(t.MAP_LINE) l
                            WHERE t.map_name='{self.game_map}'"""
        self.cursor.execute(sql_query_lines)
        for line in self.cursor:
            first_city:int = line[0]
            second_city:int = line[1]
            index:int = 0
            indice_first_city:int = -1
            indice_second_city:int = -1
            first_city_capital:bool = False
            second_city_capital:bool = False
            for city in self.cities:
                if(city[0] == first_city):
                    indice_first_city = index
                elif(city[0] == second_city):
                    indice_second_city = index
                elif(self.capital[0] == first_city):
                    first_city_capital = True
                elif(self.capital[0] == second_city):
                    second_city_capital = True
                index = index + 1
            if(first_city_capital):
                self.roads.append([self.capital, self.cities[indice_second_city], line[2]])
            elif(second_city_capital):
                self.roads.append([self.cities[indice_first_city], self.capital, line[2]])
            else:
                self.roads.append([self.cities[indice_first_city], self.cities[indice_second_city], line[2]])
            
        self.cursor.close()

    def create_game(self):
        """Create the main menu screen, the player is able to choose the map with that screen
        """
        self.root.title("Concordia")
        dimensions: Tuple[int, int] = get_monitors()[0]
        self.root.geometry(f"{dimensions.width}x{dimensions.height}")

        self.player_number = None
        self.ai_number = None
        self.ai_difficulty = None
        self.game_map = None

        image: Image.Image = Image.open("Code/src/Images/fond.png")
        image = image.resize((dimensions.width, dimensions.height), Image.LANCZOS) 
        self.photo = ImageTk.PhotoImage(image)

        label:tk.Label = tk.Label(self.root, image=self.photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.imperium_button = tk.Button(self.root, text="Imperium", command=lambda: self.player_configuration("Imperium", 5), font=("Helvetica", 24))
        self.imperium_button.place(x=dimensions.width // 2 - 150, y=dimensions.height // 2 - 60, width=300, height=120)
        self.italy_button = tk.Button(self.root, text="Italia", command=lambda: self.player_configuration("Italia", 4), font=("Helvetica", 24))
        self.italy_button.place(x=dimensions.width // 2 - 150, y=dimensions.height // 2 + 100, width=300, height=120)


    def player_configuration(self, name: str, max_players: int):
        """The popup that permit to the player to chose the number of players (need to get the min player and max player from SQL Request ToDo)

        Args:
            name (str): name of the map
            max_players (int): the max players that the player can choose (delete after sql request)
        """
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
        """The popup that permit to the player to chose the number of AI

        Args:
            player_number (str): The number of player that have been choosed by the player
            max_players (int): the max players (AI+Human) that the player can choose (delete after sql request)
            windows (tk.Toplevel): The precedent pop-up that get instantly closed
        """
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
        """The popup that permit to the player to chose the AI difficulty

        Args:
            ai_number (str): The number of AI that the player choosed
            windows (tk.Toplevel): The precedent pop-up that get instantly closed
        """
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
        """Activate the main menu button if the player close a popup (the button get desactivate if a popup is open)

        Args:
            windows (tk.Toplevel): The pop-up that get closed
        """
        windows.destroy()
        self.imperium_button.configure(state="normal")
        self.italy_button.configure(state="normal")
        windows.destroy()

    def game_screen(self, ai_difficulty: str, windows: tk.Toplevel):
        """Create and display the main game screen

        Args:
            ai_difficulty (str): difficulty of the AI that the player have choosen
            windows (tk.Toplevel): The precedent pop-up that get instantly closed
        """
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

        self.charge_map()

        max_x:int = 0
        max_y:int = 0

        for city in self.cities:
            nom, x, y = city
            max_x = max(max_x, x)  
            max_y = max(max_y, y) 

        coeff_difference_x:float = (dimensions.width - border_width * 4) / max_x
        coeff_difference_y:float = (dimensions.height * 0.75 - border_width * 4) / max_y

        canvas.create_oval((self.capital[1] * coeff_difference_x) + border_width - 10, (self.capital[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) - 10, (self.capital[1] * coeff_difference_x) + border_width + 10, (self.capital[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) + 10, fill="red")
        canvas.create_text((self.capital[1] * coeff_difference_x) + border_width, (self.capital[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) + 15, text=self.capital[0], font=("Helvetica", 8))

        for city in self.cities:
            canvas.create_oval((city[1] * coeff_difference_x) + border_width - 10, (city[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) - 10, (city[1] * coeff_difference_x) + border_width + 10, (city[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) + 10, fill="black")
            canvas.create_text((city[1] * coeff_difference_x) + border_width, (city[2] * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) + 15, text=city[0], font=("Helvetica", 8))

        way_list = []
        for way in self.roads:
            first_coordinate, second_coordinate, transport_mode = way

            if(transport_mode == "land"):
                color:str = "lightgreen"
            elif(transport_mode == "sea"):
                color:str = "blue"
            else:
                color:str = "gray"

            similar_road_number:int = 0
            for past_way in way_list:
                past_first_coordinate, past_second_coordinate, past_transport_mode = past_way
                if(first_coordinate == past_first_coordinate and second_coordinate == past_second_coordinate):
                    similar_road_number = similar_road_number + 1

            if similar_road_number == 0:
                canvas.create_line(
                    (first_coordinate[1] * coeff_difference_x) + border_width,
                    (first_coordinate[2] * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    (second_coordinate[1] * coeff_difference_x) + border_width,
                    (second_coordinate[2] * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    fill=color,
                    width=2
                )
                way_list.append(way)
            elif similar_road_number == 1:
                middle_x = (first_coordinate[1] + second_coordinate[1]) / 2
                middle_y = (first_coordinate[2] + second_coordinate[2]) / 2 + 30

                canvas.create_line(
                    (first_coordinate[1] * coeff_difference_x) + border_width,
                    (first_coordinate[2] * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    (middle_x * coeff_difference_x) + border_width,
                    (middle_y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    fill=color,
                    width=2
                )
                canvas.create_line(
                    (middle_x * coeff_difference_x) + border_width,
                    (middle_y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    (second_coordinate[1] * coeff_difference_x) + border_width,
                    (second_coordinate[2] * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    fill=color,
                    width=2
                )
                way_list.append(way)
            elif similar_road_number == 2:
                middle_x = (first_coordinate[1] + second_coordinate[1]) / 2
                middle_y = (first_coordinate[2] + second_coordinate[2]) / 2 - 30

                canvas.create_line(
                    (first_coordinate[1] * coeff_difference_x) + border_width,
                    (first_coordinate[2] * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    (middle_x * coeff_difference_x) + border_width,
                    (middle_y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    fill=color,
                    width=2
                )
                canvas.create_line(
                    (middle_x * coeff_difference_x) + border_width,
                    (middle_y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    (second_coordinate[1] * coeff_difference_x) + border_width,
                    (second_coordinate[2] * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    fill=color,
                    width=2
                )
                way_list.append(way)

if __name__ == "__main__":
    game_controller = GameManager()
