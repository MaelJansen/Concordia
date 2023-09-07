import unittest
from Code.src.Pieces import *
from Code.src.Map import *

class PieceTest:
    pass

class ColonistTest(unittest.TestCase):

    def test_move(self):
        way_colonist: Way
        colonist_test: Colonist
        way_colonist = Way("ground")
        colonist_test = Colonist("ground","blue")
        self.assertTrue(colonist_test.colonist_way is None)
        colonist_test.move(way_colonist)
        self.assertTrue(colonist_test.colonist_way == way_colonist)
        pass

class RessourceTest(unittest.TestCase):

    def test_get_info(self):
        test_resource: Resource
        test_resource = Resource(1,1,"brick",1,"green","brick")
        result = test_resource.get_info()
        info = f"Resource: brick\n"
        info += f"Type: brick\n"
        info += f"Color: green\n"
        info += f"Bonus Value: 1\n"
        info += f"Price: 1\n"
        info += f"Build Cost: 1\n"
        self.assertEqual(info, result)
        pass