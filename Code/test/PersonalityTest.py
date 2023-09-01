import unittest
import typing
from Code.src.Personality import Specialist
from Code.src.Player import *
from Code.src.Map import *

class PersonalityTest:
    pass

class ArchitectTest:
    pass

class Colonist_Test:
    
 def test_colonist(self):
    player: Player = Player(0, 0, (12, 14, 15))
    city: City = City("I", (12, 14, 15))

    city.add_house(player)

    player.my_store_house = ({"wheat": 1, "tools": 1})

    colonist_count: int = 2 
    for _ in range(colonist_count):
        colonist: Colonist = Colonist("Colonist", "Colonist", None)
        player.add_card(colonist)

    colonist.personality_action()

    expected_sesterces: int = 5 + colonist_count  
    self.assertEqual(player.get_sesterces(), expected_sesterces)

class ConcordiaTest:
    pass

class ConsulTest:
    pass

class DiplomatTest:
    pass

class MercatorTest:
    pass

class PrefectTest:
    
    
    def test_perfect(self): 
        player: Player = Player(0, 0, (12, 14, 15))
        province: Province = Province("I", (12, 14, 15))

        player.add_province_token(province)

        choice: str = "bonuses_and_products"  

        player.return_province_token(choice)

        if choice == "bonuses_and_products":
            expected_bonuses = {"wood": 2, "clay": 1, "wheat": 3}  
            expected_products = {"wood": 4, "clay": 2, "wheat": 5}  
            self.assertEqual(player.get_production_bonuses(), expected_bonuses)
            self.assertEqual(player.get_province_products(), expected_products)
        elif choice == "coins":
            for province in player.get_provinces():
                self.assertTrue(province.is_active())
            expected_coins: int = 10  
            self.assertEqual(player.get_sesterces(), expected_coins)


class PrefectusMagnusTest:
    pass

class SenatorTest:
    pass

class SpecialistTest:
    
    def test_specialist(self):
        specialist: Specialist = Specialist("Mason","Specialist",null)
        
        player: Player = Player(0,0, (12,14,15)) 
        player.add_card(specialist)
        
        city: City = City("I", (12,14,15))
        city.add_house(player)
        
        specialist.personality_action()
        self.assertEqual(player.my_store_house[0].type, "brick")
        
        
    def test_specialist2(self):
        specialist: Specialist = Specialist("Mason","Specialist",null)
        
        player: Player = Player(0,0, (12,14,15)) 
        player.add_card(specialist)
        
        city: City = City("I", (12,14,15))
        city.add_house(player)
        
        specialist.personality_action()
        self.assertEqual(player.my_store_house[0].type, "brick")
        
        specialist.personality_action()
        self.assertEqual(player.my_store_house[1].type, null)
        

class TribuneTest:
    pass