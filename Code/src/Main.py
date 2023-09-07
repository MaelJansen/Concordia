from ast import List, Set, Tuple
from math import atan2, degrees
import tkinter as tk
import pprint
from tkinter import ttk
from PIL import ImageTk, Image
from screeninfo import get_monitors
from Map import City, CityToken, Line, Map
from Players import Player
from Cards import Card, MarketPlace
from Map import Map
from typing import Type
import oracledb
import Pieces


class GameManager:
    """
    A class to control the game 

    ...

    Attributes
    ----------
    player_controller : PlayerManager
    game_map : Map
    player_list : List<Player>
    capital : City
    cities : List[City]
    roads : Set[Line]
    market_place : MarketPlace
    current_player_index : int
    """

    def __init__(self):
        self.player_controller = None
        self.game_map: Map
        self.player_list:List[Player] = []
        self.capital: City
        self.cities: List[City] = []
        self.roads: Set[Line] = []
        self.market_place:MarketPlace = MarketPlace()
        self.current_player_index = 0  # Index of the current player

        self.connection = oracledb.connect(
            user="ETD",
            password="ETD",
            host="localhost",
            port=1521,
            sid="IUT12c"
        )
        self.cursor = self.connection.cursor()
        self.initialization_script()
        

    def initialization_script(self):
        self.createInterface()

    def createInterface(self):
        """This method creates the interface of the game
        """
        root = tk.Tk()
        concordia_screen = Screen(root,self)
        root.mainloop()

    def start_game(self, player_number:int):
        """This method starts the game

        Args:
            player_number (int): number of players
        """
        # Initialize the game, set up the map, create players, etc.
        self.get_resource_setup_data()
        self.create_players(player_number) 
        self.setup_players()


    def create_players(self, num_players:int):
        """
        This method create the players according to the number of players
        Args:
            num_players (int): number of players
        """
        for player_num in range(num_players):
            self.player_list.append(Player())  # Replace with actual player creation

    def setup_players(self):
        """
        This method setup the players according to the database
        """
        player_setup_data = self.get_player_setup_data()

        # Assign player setup data to each player
        for player_num in range (0,len(self.player_list)):
            current_player = self.player_list[player_num]

            colonist_data = player_setup_data[0]
            current_player.setup_colonists(colonist_data)

            goods_data = player_setup_data[1]
            current_player.setup_goods(goods_data)

            houses_data = player_setup_data[2]
            current_player.setup_houses(houses_data)

            cards_data = player_setup_data[3]
            current_player.setup_cards(cards_data)

            sestertii_data = player_setup_data[4][player_num]
            current_player.setup_sestertii(sestertii_data)

    def get_player_setup_data(self):
        """
        This method get the data of the players from the database
        """
        sql_query_colonists = f"""SELECT spc.setup_p_colon_way,
                            spc.setup_p_colon_n_colonists,
                            spc.setup_p_colon_n_colonists_cap
                            FROM T_Concordia t, table(t.concordia_setup_player.setup_p_colonist) spc"""
        
        self.cursor.execute(sql_query_colonists)
        colonists_data=[]
        for row in self.cursor:
            temp_colonists_data = [row[0], row[1], row[2]]
            colonists_data.append(temp_colonists_data)

        sql_query_goods = f"""SELECT spg.setup_p_good_good ,
                            spg.setup_p_good_n_goods
                            FROM T_Concordia t, table(t.concordia_setup_player.setup_p_good) spg"""
        
        self.cursor.execute(sql_query_goods)
        goods_data=[]
        for row in self.cursor:
            temp_goods_data = [row[0], row[1]]
            goods_data.append(temp_goods_data)

        sql_query_cards = f"""SELECT spc.setup_p_card_card ,
                            spc.setup_p_card_n_copies
                            FROM T_Concordia t, table(t.concordia_setup_player.setup_p_card) spc """
        self.cursor.execute(sql_query_cards)
        cards_data = []
        for row in self.cursor:
            temp_cards_data = [row[0], row[1]]
            cards_data.append(temp_cards_data)

        sql_query_houses = f"""SELECT t.concordia_setup_player.setup_p_n_houses
                            FROM T_Concordia t"""
        self.cursor.execute(sql_query_houses)
        houses_data = []
        for row in self.cursor:
            temp_houses_data = [row[0]]
            houses_data.append(temp_houses_data)

        sql_query_sestertii = f"""SELECT sps.setup_p_se_order_of_play ,
                                sps.setup_p_se_n_sestertii ,
                                sps.setup_p_se_n_sestertii_variant
                                FROM T_Concordia t, table(t.concordia_setup_player.setup_p_sestertius) sps"""
        
        self.cursor.execute(sql_query_sestertii)
        sestertii_data = []
        for row in self.cursor:
            temp_sestersii_data = [row[0], row[1], row[2]]
            sestertii_data.append(temp_sestersii_data)

        all_player_data= colonists_data, goods_data, houses_data, cards_data, sestertii_data
        return all_player_data
    
    def get_resource_setup_data(self):
        """
        This method get the data of the resources from the database and create the resource type
        """
        sql_query_goods = f"""SELECT t.good_name name,
                                t.good_value value,
                                good_color color,
                                good_n_sestertii_bonus_marker n_sestertii_bonus_marker,
                                good_n_sestertii_build_cost n_sestertii_build_cost
                                FROM T_Concordia, TABLE(T_Concordia.concordia_good) t"""
        
        self.cursor.execute(sql_query_goods)
        goods_data=[]
        for row in self.cursor:
            temp_goods_data = [row[0], row[1], row[2], row[3], row[4]]
            goods_data.append(temp_goods_data)
        Pieces.ResourceType.setup_resource_types(goods_data)

    def start_next_player_turn(self):
        """
        This method start the turn of the next player
        """
        # Get the current player
        current_player = self.player_list[self.current_player_index]

        # Start the player's turn (to be implemented in PlayerController)
        self.player_controller.start_player_turn(current_player)

        # Increment the current player index
        self.current_player_index = (self.current_player_index + 1) % len(self.player_list)

    def end_game(self):
        # End the game, calculate scores, display results, etc.
        pass
   

    def calculate_victory_points(self):
        """This method calculate the victory points of each player and return a dictionary with
          the name of the player and his victory points
        """
        vps = {} 

        for player in self.player_list:
            total_vps: int = 0
            player = Type[Player](player)
            
            if player.peaceful_end:
                total_vps += 7
            
            cash_money: int = player.money
            goods_value: int = sum(goods_price * quantity for goods_price, quantity in player.storehouse.items())
            total_cash_value: int= cash_money + goods_value
            vps_vesta: int = total_cash_value // 10
            total_vps += vps_vesta

            non_brick_cities = [house for house in player.my_houses if house.assigned_city_token.assigned_ressource != "brick"]
            total_vps += len(non_brick_cities)

            produced_resources = set()
            for house in player.my_houses:
                assigned_resource = house.houses.assigned_city_token.assigned_resource
                if assigned_resource not in produced_resources:
                    produced_resources.add(assigned_resource)

            total_vps += len(produced_resources) * 2

            vps_mars = len(player.my_colonist) * 2
            total_vps += vps_mars

            i: int = 0
            province_list: list = []

            for i in range(len(player.my_houses)):
                total_vps += 1

            for provinces in self.game_map.map_provinces:
                for city in provinces:
                    if player.my_houses[i] == city and provinces not in province_list:
                        province_list.append(provinces)

            total_vps += len(province_list)

            vps[player.name] = total_vps
            player.n_point = total_vps

        return vps
    
    def charge_map(self):
        """This method uses SQL resquests to get the capital, the cities and the ways of the map that have been choosed by the player to place them in list. The lists
        will be used to display the city, ways... on the map. 
        """
        sql_query_capital = f"""SELECT t.MAP_CAPITAL.CITY_NAME AS CAPITAL, t.MAP_CAPITAL.CITY_COORDINATES.X as x, t.MAP_CAPITAL.CITY_COORDINATES.Y as y
                            FROM T_Concordia, TABLE(T_Concordia.concordia_map) t 
                            WHERE t.map_name='{self.game_map.name}'"""
        self.cursor.execute(sql_query_capital)
        for row in self.cursor:
            self.capital = City(CityToken(), row[0], row[1], row[2])
            
        sql_query_cities = f"""SELECT c.CITY_NAME as city_name,
                            c.CITY_COORDINATES.X as x,
                            c.CITY_COORDINATES.Y as y
                            FROM T_Concordia, TABLE(T_Concordia.concordia_map) t , TABLE(t.MAP_PROVINCE) p , TABLE(p.province_city) c
                            WHERE t.map_name='{self.game_map.name}'"""
        self.cursor.execute(sql_query_cities)
        for city in self.cursor:
            temp_city = City(CityToken(), city[0], city[1], city[2])
            self.cities.append(temp_city)

        sql_query_lines = f"""SELECT l.line_city_1 city1, l.line_city_2 city2, l.line_way way
                            FROM T_Concordia, TABLE(T_Concordia.concordia_map) t, TABLE(t.MAP_LINE) l
                            WHERE t.map_name='{self.game_map.name}'"""
        self.cursor.execute(sql_query_lines)
        for line in self.cursor:
            first_city: int = line[0]
            second_city: int = line[1]
            index: int = 0
            indice_first_city: int = -1
            indice_second_city: int = -1
            first_city_capital: bool = False
            second_city_capital: bool = False
            for city in self.cities:
                if(city.name == first_city):
                    indice_first_city = index
                elif(city.name == second_city):
                    indice_second_city = index
                elif(self.capital.name == first_city):
                    first_city_capital = True
                elif(self.capital.name == second_city):
                    second_city_capital = True
                index = index + 1
            if(first_city_capital):
                self.roads.append(Line(self.capital, self.cities[indice_second_city], line[2]))
            elif(second_city_capital):
                self.roads.append(Line(self.cities[indice_first_city], self.capital, line[2]))
            else:
                self.roads.append(Line(self.cities[indice_first_city], self.cities[indice_second_city], line[2]))
                
    def charge_cards(self):
        sql_query_display_area = f"""SELECT t.*
                                FROM T_Concordia, TABLE(T_Concordia.concordia_display_area) t"""
        self.cursor.execute(sql_query_display_area)
        for display_area in self.cursor:
            self.market_place.display_area.append([display_area[0], display_area[1], display_area[2], display_area[3]])

class PlayerController:
    def play(self, player: object, card: Card):
        """Play a card of a player

        Args:
        player (Player) : The player who play
        card (Card) : The card playing
        """
        if card in player.hand:
            player.hand.remove(card)
            player.discard_pile.append(card)
            player.play_card(card)

class Screen:
    """This class create the display of the game (main menu, gameplay...)
    """
    def __init__(self, root: tk.Tk, game_manager: GameManager):
        """Initialize an instance of the screen class.

        Args:
        root (tk.Tk): An instance of the main application window.
        """
        self.game_manager = game_manager
        self.root: tk.Tk = root
        self.ai_number: int = 0
        self.ai_difficulty: str = ""
        self.maps: list[str] = []
        self.map_button: List[tk.Button]
        self.player_number:int
        self.create_game()

    def create_game(self):
        """Create the main menu screen, the player is able to choose the map with that screen
        """
        self.root.title("Concordia")
        dimensions: Tuple[int, int] = get_monitors()[0]
        self.root.geometry(f"{dimensions.width}x{dimensions.height}")

        self.game_manager.player_list = []
        self.ai_number = None
        self.ai_difficulty = None

        image: Image.Image = Image.open("Code/src/Images/fond.png")
        image = image.resize((dimensions.width, dimensions.height), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)

        label: tk.Label = tk.Label(self.root, image=self.photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.imperium_button = tk.Button(self.root, text="Imperium", command=lambda: self.player_configuration("Imperium", 2, 5), font=("Helvetica", 24))
        self.imperium_button.place(x=dimensions.width // 2 - 150, y=dimensions.height // 2 - 60, width=300, height=120)
        self.italy_button = tk.Button(self.root, text="Italia", command=lambda: self.player_configuration("Italia", 2, 4), font=("Helvetica", 24))
        self.italy_button.place(x=dimensions.width // 2 - 150, y=dimensions.height // 2 + 100, width=300, height=120)
        self.europe_button = tk.Button(self.root, text="Europe", command=lambda: self.player_configuration("EU", 2, 4), font=("Helvetica", 24))
        self.europe_button.place(x=dimensions.width // 2 - 150, y=dimensions.height // 2 + 260, width=300, height=120)


    def player_configuration(self, name: str, min_player:int, max_players: int):
        """The popup that permit to the player to chose the number of players (need to get the min player and max player from SQL Request ToDo)

        Args:
            name (str): name of the map
            max_players (int): the max players that the player can choose (delete after sql request)
        """
        self.game_manager.game_map = Map(name, min_player, max_players)

        self.imperium_button.configure(state="disabled")
        self.italy_button.configure(state="disabled")
        self.europe_button.configure(state="disabled")

        windows: tk.Toplevel = tk.Toplevel(self.root)
        windows.title(f"{name} configuration")
        windows.resizable(False, False)

        windows_width: int = 300
        windows_height: int = 110

        dimensions: Tuple[int, int] = get_monitors()[0]

        x_coordinate: int = int((dimensions.width - windows_width) // 2)
        y_coordinate: int = int((dimensions.height - windows_height) // 2)

        windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

        player_number_label: tk.Label = tk.Label(windows, text="Choose the number of players :")
        player_number_label.pack()

        player_number_box:ttk.Combobox = ttk.Combobox(windows, values=[str(i) for i in range(self.game_manager.game_map.max_player + 1)])
        player_number_box.set("0")
        player_number_box.pack(padx=20, pady=10)

        bouton:tk.Button = tk.Button(windows, text="Validate", command=lambda: self.ai_configuration(player_number_box.get(), windows))
        bouton.pack(pady=10)

        windows.protocol("WM_DELETE_WINDOW", lambda: self.on_screen_close(windows))

    def ai_configuration(self, player_number: str, windows: tk.Toplevel):
        """The popup that permit to the player to chose the number of AI

        Args:
            player_number (str): The number of player that have been choosed by the player
            max_players (int): the max players (AI+Human) that the player can choose (delete after sql request)
            windows (tk.Toplevel): The precedent pop-up that get instantly closed
        """
        self.player_number = int(player_number)
        if self.player_number != self.game_manager.game_map.max_player:
            windows.destroy()
            self.imperium_button.configure(state="disabled")
            self.italy_button.configure(state="disabled")
            self.europe_button.configure(state="disabled")

            max_ia: int = self.game_manager.game_map.max_player - len(self.game_manager.player_list)

            if len(self.game_manager.player_list) == 0:
                min_ia: int = 2
            elif len(self.game_manager.player_list) == 1:
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
            if len(self.game_manager.player_list) > 1:
                ai_number_box.set("0")
            elif len(self.game_manager.player_list) == 1:
                ai_number_box.set("1")
            else:
                ai_number_box.set("2")
            ai_number_box.pack(padx=20, pady=10)

            bouton: tk.Button = tk.Button(windows, text="Validate",
                                          command=lambda: self.ai_difficulty_configuration(ai_number_box.get(),
                                                                                           windows))
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
        if (self.ai_number != 0):
            windows.destroy()
            self.imperium_button.configure(state="disabled")
            self.italy_button.configure(state="disabled")
            self.europe_button.configure(state="disabled")

            windows: tk.Toplevel = tk.Toplevel(self.root)
            windows.title("AI difficulty configuration")
            windows.resizable(False, False)

            windows_width: int = 300
            windows_height: int = 110

            dimensions: Tuple[int, int] = get_monitors()[0]

            x_coordinate: int = int((dimensions.width - windows_width) // 2)
            y_coordinate: int = int((dimensions.height - windows_height) // 2)

            windows.geometry(f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

            ai_difficulty_label: tk.Label = tk.Label(windows, text="Choose the AI difficuly :")
            ai_difficulty_label.pack()

            ai_difficulty_box: ttk.Combobox = ttk.Combobox(windows, values=["Esay", "Medium", "Difficult"])
            ai_difficulty_box.set("Medium")
            ai_difficulty_box.pack(padx=20, pady=10)

            bouton: tk.Button = tk.Button(windows, text="Validate",
                                          command=lambda: self.game_screen(ai_difficulty_box.get(), windows))
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
        self.europe_button.configure(state="normal")
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
        
        self.game_manager.start_game(self.player_number)

        self.root.title("Concordia")
        dimensions: Tuple[int, int] = get_monitors()[0]
        self.root.geometry(f"{dimensions.width}x{dimensions.height}")

        canvas: tk.Canvas = tk.Canvas(self.root, width=dimensions.width, height=dimensions.height)
        canvas.pack()

        border_width: int = 20
        canvas.create_line(border_width, dimensions.height * 0.25, dimensions.width - border_width,
                           dimensions.height * 0.25, fill="black", width=3)
        canvas.create_line(dimensions.width * 0.33, border_width, dimensions.width * 0.33, dimensions.height * 0.25,
                           fill="black", width=3)

        self.game_manager.charge_map()

        max_x: int = 0
        max_y: int = 0

        for city in self.game_manager.cities:
            x = city.x
            y = city.y
            max_x = max(max_x, x)  
            max_y = max(max_y, y) 

        coeff_difference_x: float = (dimensions.width - border_width * 4) / max_x
        coeff_difference_y: float = (dimensions.height * 0.75 - border_width * 4) / max_y

        canvas.create_oval((self.game_manager.capital.x * coeff_difference_x) + border_width - 10, (self.game_manager.capital.y * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) - 10, (self.game_manager.capital.x * coeff_difference_x) + border_width + 10, (self.game_manager.capital.y * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) + 10, fill="red")
        canvas.create_text((self.game_manager.capital.x * coeff_difference_x) + border_width, (self.game_manager.capital.y * coeff_difference_y) + (border_width + dimensions.height*0.25 + 3) + 15, text=self.game_manager.capital.name, font=("Helvetica", 8))

        transformed_cities: List[City] = list(map(lambda city: City(CityToken(), city.name, (city.x * coeff_difference_x) + border_width, city.y * coeff_difference_y + (border_width + dimensions.height * 0.25 + 3)), self.game_manager.cities))

        for city in transformed_cities:
            name = city.name
            x = city.x 
            y = city.y
            canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="black")
            canvas.create_text(x, y + 15, text=name, font=("Helvetica", 8))


        way_list = []
        for way in self.game_manager.roads:

            if(way.line_way.name == "land"):
                color:str = "lightgreen"
            elif(way.line_way.name == "sea"):
                color:str = "blue"
            else:
                color: str = "gray"

            similar_roads = filter(lambda past_way: way.city_list[0] == past_way.city_list[0] and way.city_list[1] == past_way.city_list[1], way_list)
            similar_road_number = len(list(similar_roads))

            if similar_road_number == 0:
                canvas.create_line(
                    (way.city_list[0].x * coeff_difference_x) + border_width,
                    (way.city_list[0].y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    (way.city_list[1].x * coeff_difference_x) + border_width,
                    (way.city_list[1].y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    fill=color,
                    width=2
                )
                way_list.append(way)
            elif similar_road_number == 1:
                middle_x = (way.city_list[0].x + way.city_list[1].x) / 2 - 40
                middle_y = (way.city_list[0].y + way.city_list[1].y) / 2 + 35

                canvas.create_line(
                    (way.city_list[0].x * coeff_difference_x) + border_width,
                    (way.city_list[0].y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    (middle_x * coeff_difference_x) + border_width,
                    (middle_y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    fill=color,
                    width=2
                )
                canvas.create_line(
                    (middle_x * coeff_difference_x) + border_width,
                    (middle_y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    (way.city_list[1].x * coeff_difference_x) + border_width,
                    (way.city_list[1].y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    fill=color,
                    width=2
                )
                way_list.append(way)
            elif similar_road_number == 2:
                middle_x = (way.city_list[0].x + way.city_list[1].x) / 2 - 40
                middle_y = (way.city_list[0].y + way.city_list[1].y) / 2 - 35

                canvas.create_line(
                    (way.city_list[0].x * coeff_difference_x) + border_width,
                    (way.city_list[0].y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    (middle_x * coeff_difference_x) + border_width,
                    (middle_y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    fill=color,
                    width=2
                )
                canvas.create_line(
                    (middle_x * coeff_difference_x) + border_width,
                    (middle_y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    (way.city_list[1].x * coeff_difference_x) + border_width,
                    (way.city_list[1].y * coeff_difference_y) + (border_width + dimensions.height * 0.25 + 3),
                    fill=color,
                    width=2
                )
                way_list.append(way)
                
        piece_counts = {}
        for piece in self.game_manager.player_list[0].my_store_house.my_pieces:
            if piece in piece_counts:
                piece_counts[piece] += 1
            else:
                piece_counts[piece] = 1

        heightCoeff = 0.05
        width = 0
        for piece, count in piece_counts.items():
            canvas.create_text(border_width * 2 + width, dimensions.height * heightCoeff, text=f"{piece}: {count}", font=("Helvetica", 9), anchor="w")
            heightCoeff += 0.05
            if(heightCoeff == 0.25):
                heightCoeff = 0.05
                width = width + dimensions.width * 0.15
                
        self.game_manager.charge_cards()
                
        for i in range(0, 7):
            x1 = 0.33 + ((0.77 / 8) * (i + 1)) - 0.017
            if(self.game_manager.market_place.display_area[i][0] == 1):
                x2 = 0.33 + ((0.77 / 8) * (i + 1) - 0.01)
            else:
                x2 = 0.33 + ((0.77 / 8) * (i + 1)) - 0.018
            canvas.create_line(dimensions.width * x1 + border_width, border_width, dimensions.width * x1 + border_width, dimensions.height * 0.25,
                           fill="black", width=2)
            
            canvas.create_text(dimensions.width * (x2 - 0.08), dimensions.height * 0.05, text="Personality : Mercator", font=("Helvetica", 8), anchor="w")
            canvas.create_text(dimensions.width * (x2 - 0.08), dimensions.height * 0.10, text="God : Minerva", font=("Helvetica", 8), anchor="w")
            canvas.create_text(dimensions.width * (x2 - 0.08), dimensions.height * 0.15, text="Price : 3 brick", font=("Helvetica", 8), anchor="w")
            
            if(self.game_manager.market_place.display_area[i][1] == "N" and self.game_manager.market_place.display_area[i][2] != None):
                canvas.create_text(dimensions.width * (x2 - 0.08), dimensions.height * 0.20, text="Display area price : " + str(self.game_manager.market_place.display_area[i][3]) + " " + self.game_manager.market_place.display_area[i][2], font=("Helvetica", 9), anchor="w")
            elif(self.game_manager.market_place.display_area[i][1] == "Y" and self.game_manager.market_place.display_area[i][2] == None):
                canvas.create_text(dimensions.width * (x2 - 0.08), dimensions.height * 0.20, text="Display area price : 1 good (any)", font=("Helvetica", 8), anchor="w")
            elif(self.game_manager.market_place.display_area[i][1] == "Y"):
                canvas.create_text(dimensions.width * (x2 - 0.08), dimensions.height * 0.20, text="Display area price : " + str(self.game_manager.market_place.display_area[i][3]) + " " + self.game_manager.market_place.display_area[i][2] + "\nand 1 good (any)", font=("Helvetica", 9), anchor="w")
            else:
                canvas.create_text(dimensions.width * (x2 - 0.08), dimensions.height * 0.20, text="Display area price : Nothing", font=("Helvetica", 8), anchor="w")
                
if __name__ == "__main__":
    # Creating a singleton game manager
    game_manager:GameManager = GameManager()    
