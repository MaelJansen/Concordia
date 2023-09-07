import copy

from Code.src.Players import Player
from Code.src.Map import *
from Code.src.Cards import Card, God
from Code.src.Personalities import *
from Code.src.Pieces import *
import unittest

class CardTest:
    pass

class GodTest(unittest.TestCase):
    def test_point_calculation(self):
        # Simulation of the end game for one player
        # cities and cities tokens creation
        test_valencia = City(Position())

        test_brick = Resource(2, 1, "brick", 1, "blue", "brick")
        test_food = Resource(2, 1, "food", 1, "grey", "food")
        test_tool = Resource(2, 1, "tool", 1, "black", "tool")
        test_cloth = Resource(2, 1, "cloth", 1, "yellow", "cloth")

        test_token = CityToken()
        test_token.assigned_resource = test_brick.name
        test_token1 = CityToken()
        test_token1.assigned_resource = test_brick.name
        test_token2 = CityToken()
        test_token2.assigned_resource = test_brick.name
        test_token3 = CityToken()
        test_token3.assigned_resource = test_food.name
        test_token4 = CityToken()
        test_token4.assigned_resource = test_food.name
        test_token5 = CityToken()
        test_token5.assigned_resource = test_food.name
        test_token6 = CityToken()
        test_token6.assigned_resource = test_food.name
        test_token7 = CityToken()
        test_token7.assigned_resource = test_tool.name
        test_token8 = CityToken()
        test_token8.assigned_resource = test_tool.name
        test_token9 = CityToken()
        test_token9.assigned_resource = test_tool.name
        test_token10 = CityToken()
        test_token10.assigned_resource = test_cloth.name
        test_token11 = CityToken()
        test_token11.assigned_resource = test_cloth.name

        test_valencia.assigned_city_token = test_token
        test_petra = City(Position())
        test_petra.assigned_city_token = test_token1       
        test_burdigal = City(Position())
        test_burdigal.assigned_city_token = test_token2
        test_massilia = City(Position())
        test_massilia.assigned_city_token = test_token3
        test_leptis_magna = City(Position())
        test_leptis_magna.assigned_city_token = test_token4
        test_cyrene = City(Position())
        test_cyrene.assigned_city_token = test_token5
        test_alexandria = City(Position())
        test_alexandria.assigned_city_token = test_token6
        test_tyros = City(Position())
        test_tyros.assigned_city_token = test_token7
        test_antiochia = City(Position())
        test_antiochia.assigned_city_token = test_token8
        test_sinope = City(Position())
        test_sinope.assigned_city_token = test_token9
        test_tomis = City(Position())
        test_tomis.assigned_city_token = test_token10
        test_vindobona = City(Position())
        test_vindobona.assigned_city_token = test_token11


        test_province1 = Province(test_food)
        test_province1.my_cities = [test_petra, test_tyros, test_vindobona]
        test_province2 = Province(test_brick)
        test_province2.my_cities =[test_valencia, test_sinope, test_antiochia]
        test_province3 = Province(test_tool)
        test_province3.my_cities =[test_alexandria, test_cyrene, test_leptis_magna]

        player_test = Player()

        # hand creation 
        test_personality_concordia = Concordia(player_test)
        test_personality_prefect = Prefect(player_test)
        test_personality_architect = Architect(player_test)
        test_personality_senator = Senator(player_test)
        test_personality_mercator = Mercator(player_test)
        test_personality_tribune = Tribune(player_test)
        test_personality_farmer = Specialist(player_test, test_food)
        test_personality_farmer.name = "Farmer"

        test_concordia = Card()
        test_concordia.my_personality = test_personality_concordia
        test_prefect1 = Card()
        test_prefect1.my_personality = test_personality_prefect
        test_prefect2 = Card()
        test_prefect2.my_personality = test_personality_prefect
        test_prefect3 = Card()
        test_prefect3.my_personality = test_personality_prefect
        test_prefect4 = Card()
        test_prefect4.my_personality = test_personality_prefect
        test_architect1 = Card()
        test_architect1.my_personality = test_personality_architect
        test_architect2 = Card()
        test_architect2.my_personality = test_personality_architect
        test_senator = Card()
        test_senator.my_personality = test_personality_senator
        test_mercator1 = Card()
        test_mercator1.my_personality = test_personality_mercator
        test_mercator2 = Card()
        test_mercator2.my_personality = test_personality_mercator
        test_tribune1 = Card()
        test_tribune1.my_personality = test_personality_tribune
        test_tribune2 = Card()
        test_tribune2.my_personality = test_personality_tribune
        test_tribune3 = Card()
        test_tribune3.my_personality = test_personality_tribune
        test_farmer = Card()
        test_farmer.my_personality = test_personality_farmer
        test_god = God("minerva")
        test_god.victory_points = 3
        test_farmer.my_diety = test_god

        # pieces (colonists and resources) creation

        test_cloth1 = copy.copy(test_cloth)
        test_cloth1.name = "clothe"
        test_tool1 = copy.copy(test_tool)
        test_tool1.name = "tool"
        test_tool2 = copy.copy(test_tool)
        test_tool2.name = "tool"
        test_tool3 = copy.copy(test_tool)
        test_tool3.name = "tool"
        test_brick1 = copy.copy(test_brick)
        test_brick1.name = "brick"

        # Colonist creation 
        test_colonist1 = Colonist("ground","blue")
        test_colonist2 = Colonist("ground","blue")
        test_colonist3 = Colonist("ground","blue")
        test_colonist4 = Colonist("ground","blue")
        test_colonist5 = Colonist("ground","blue")

        # player creation
        player_test.my_houses = [test_valencia, test_alexandria, test_antiochia, test_burdigal,
                             test_cyrene, test_leptis_magna, test_massilia, test_petra, test_sinope, 
                             test_tomis, test_vindobona, test_tyros]
        player_test.money = 13
        player_test.hand = [test_concordia, test_prefect1, test_prefect2, test_prefect3, test_prefect4,
                            test_architect1, test_architect2, test_senator, test_mercator1,
                            test_mercator2, test_tribune1, test_tribune2, test_tribune3, test_farmer]
        player_test.my_colonist = [test_colonist1, test_colonist2, test_colonist3, test_colonist4, test_colonist5]
        player_test.my_store_house = [test_cloth1, test_tool1, test_tool2, test_tool3,
                                      test_brick1]
        
        # God creation
        test_vesta = God("Vesta")
        test_jupiter = God("Jupiter")
        test_saturnus = God("Saturnus")
        test_mercurius = God("Mercurius")
        test_mars = God("Mars")
        test_minerva = God("Minerva")

        # final score for each god
        score_vesta = 2
        score_jupiter = score_vesta + 9
        score_saturnus = score_jupiter + 9
        score_mercurius = score_saturnus + 8
        score_mars = score_mercurius + len(player_test.my_colonist)
        score_minerva = score_mars + 4*3

        test_map = Map(1,4)
        test_map.my_provinces = [test_province1, test_province2, test_province3]
        res = test_vesta.point_calculation(player_test, test_map)
        #Compare the final score with the calculated score
        self.assertEqual(score_vesta, player_test.n_point)
        test_jupiter.point_calculation(player_test, test_map)
        self.assertEqual(score_jupiter, player_test.n_point)
        test_saturnus.point_calculation(player_test, test_map)
        self.assertEqual(score_saturnus, player_test.n_point)
        test_mercurius.point_calculation(player_test, test_map)
        self.assertEqual(score_mercurius, player_test.n_point)
        test_mars.point_calculation(player_test, test_map)
        self.assertEqual(score_mars, player_test.n_point)
        test_minerva.point_calculation(player_test, test_map)
        self.assertEqual(score_minerva, player_test.n_point)
        

'''city -> city token -> assigned resource'''

class MarketPlaceTest:
    pass