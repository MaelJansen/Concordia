from Player import Player
from Map import City, CityToken
from Card import Card, God
from Personality import Personality, Concordia, Architect, Consul, Mercator, Prefect, Senator, Specialist, Tribune
from Piece import Ressource, Colonist
import unittest

class CardTest:
    pass

class GodTest(unittest.TestCase):
    def point_calculation_test(self):
        # Simulation of the end game for one player
        # cities and cities tokens creation
        test_valencia = City()
        test_valencia.assigned_city_token = test_token
        test_petra = City()
        test_petra.assigned_city_token = test_token1       
        test_burdigal = City()
        test_burdigal.assigned_city_token = test_token2
        test_massilia = City()
        test_massilia.assigned_city_token = test_token3
        test_leptis_magna = City()
        test_leptis_magna.assigned_city_token = test_token4
        test_cyrene = City()
        test_cyrene.assigned_city_token = test_token5
        test_alexandria = City()
        test_alexandria.assigned_city_token = test_token6
        test_tyros = City()
        test_tyros.assigned_city_token = test_token7
        test_antiochia = City()
        test_antiochia.assigned_city_token = test_token8
        test_sinope = City()
        test_sinope.assigned_city_token = test_token9
        test_tomis = City()
        test_tomis.assigned_city_token = test_token10
        test_vindobona = City()
        test_vindobona.assigned_city_token = test_token11

        test_token = CityToken()
        test_token.assigned_ressource = test_brick
        test_token1 = CityToken()
        test_token1.assigned_ressource = test_brick
        test_token2 = CityToken()
        test_token2.assigned_ressource = test_brick
        test_token3 = CityToken()
        test_token3.assigned_ressource = test_food
        test_token4 = CityToken()
        test_token4.assigned_ressource = test_food
        test_token5 = CityToken()
        test_token5.assigned_ressource = test_food
        test_token6 = CityToken()
        test_token6.assigned_ressource = test_food
        test_token7 = CityToken()
        test_token7.assigned_ressource = test_tool
        test_token8 = CityToken()
        test_token8.assigned_ressource = test_tool
        test_token9 = CityToken()
        test_token9.assigned_ressource = test_tool
        test_token10 = CityToken()
        test_token10.assigned_ressource = test_cloth
        test_token11 = CityToken()
        test_token11.assigned_ressource = test_cloth

        # hand creation 
        test_personality_concordia = Concordia()
        test_personality_prefect = Prefect()
        test_personality_architect = Architect()
        test_personality_senator = Senator()
        test_personality_mercator = Mercator()
        test_personality_tribune = Tribune()
        test_personality_farmer = Specialist()
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

        # pieces (colonists and resources) creation
        test_cloth = Ressource()
        test_cloth.name = "cloth"
        test_brick = Ressource()
        test_brick = "brick"
        test_tool = Ressource()
        test_tool.name = "tool"
        test_food = Ressource()
        test_food = "food"

        test_cloth1 = Ressource()
        test_cloth1.name = "clothe"
        test_tool1 = Ressource()
        test_tool1.name = "tool"
        test_tool2 = Ressource()
        test_tool2.name = "tool"
        test_tool3 = Ressource()
        test_tool3.name = "tool"
        test_brick1 = Ressource()
        test_brick1.name = "brick"

        # Colonist creation 
        test_colonist1 = Colonist()
        test_colonist2 = Colonist()
        test_colonist3 = Colonist()
        test_colonist4 = Colonist()
        test_colonist5 = Colonist()

        # player creation
        player_test = Player()
        player_test.house = [test_valencia, test_alexandria, test_antiochia, test_burdigal, 
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
        test_mercurius = God("Merrcurius")
        test_mars = God("Mars")
        test_minerva = God("Minerva")

        # final score for each god
        score_vesta = 3
        score_jupiter = 18
        score_saturnus = 28
        score_mercurius = 16
        score_mars = 30
        score_minerva = 12

        #Compare the final score with the calculated score
        self.assertEqual(score_vesta, test_vesta.point_calculation(player_test))
        self.assertEqual(score_jupiter, test_jupiter.point_calculation(player_test))
        self.assertEqual(score_saturnus, test_saturnus.point_calculation(player_test))
        self.assertEqual(score_mercurius, test_mercurius.point_calculation(player_test))
        self.assertEqual(score_mars, test_mars.point_calculation(player_test))
        self.assertEqual(score_minerva, test_minerva.point_calculation(player_test))
        

'''city -> city token -> assigned resource'''

class MarketPlaceTest:
    pass