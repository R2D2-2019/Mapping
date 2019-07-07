import unittest
from algorithm import Algorithms


class TestsMapping(unittest.TestCase):

    ## Testing if decimal degrees gives back the correct Time degrees
    def test_decimal_degrees_to_time_degrees(self):
        alg = Algorithms()
        self.assertEqual(alg.decimal_degrees_to_time_degrees(20.67694), {'hours': 20,'minutes': 40,'seconds': 37})

    ## Testing if Time degrees gives back the correct decimal degrees
    def test_time_degrees_to_decimal_degrees(self):
        alg = Algorithms()
        self.assertAlmostEqual(alg.time_degrees_to_decimal_degrees({'hours': 20,'minutes': 40,'seconds': 37}), 20.67694, places=5, msg=None, delta=None)

    ## Testing on the distance between Heidelberglaan 15 and the Spar university which on google maps is ~270 meters as the crow flies
    def test_measure_distance(self):
        alg = Algorithms()
        self.assertAlmostEqual(alg.measure_distance(52.084165, 5.175766, 52.084300, 5.171823), 270, places=0, msg=None, delta=None)

    ## Testing new world coordinate if you moved a X/ Y distance
    def test_calculate_new_coordinate(self):
        alg = Algorithms()
        self.assertEqual(alg.calculate_new_coordinate(52.084165, 5.175766, 0, 270), (52.084165, 6.523238926179283))

    ## Get X and Y coordinate difference of the center and obstacles seen from the lidar
    def test_from_lidar_coordinate_to_distance(self):
        alg = Algorithms()
        self.assertEqual(alg.from_lidar_to_coordinate(315, 50), [35,35])


if __name__ == '__main__':
    unittest.main()