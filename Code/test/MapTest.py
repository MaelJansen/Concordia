import unittest
from Code.src.Pieces import *
from Code.src.Map import *

class MapTest:
    pass

class ProvinceTest:
    pass

class PositionTest:
    pass

class CityTest:
    pass

class CityTokenTest:
    pass

class LineTest:
    pass

class WayTest(unittest.TestCase):

    def test_is_valid_move_for_colonist(self):
        way_colonist: Way
        colonist_test: Colonist
        colonist_test2 : Colonist
        way_colonist = Way("ground")
        colonist_test = Colonist("ground", "blue")
        colonist_test2 = Colonist("ground","green")
        self.assertTrue(way_colonist.is_valid_move_for_colonist(colonist_test))
        colonist_test2.move(way_colonist)
        self.assertTrue(way_colonist.occupant is not None)
        self.assertFalse(way_colonist.is_valid_move_for_colonist(colonist_test))
        pass