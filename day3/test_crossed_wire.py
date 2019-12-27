"""
Module to test the day 3 code.
"""

from crossed_wire import find_closest_intersection
import unittest

class Tests(unittest.TestCase):
    """Class which contains unit tests for day 3 code

    """
    def test_crossed_wire(self):
        """Tests crossed wire with online examples
        """
        self.assertEquals(find_closest_intersection("R8,U5,L5,D3", "U7,R6,D4,L4"), 6)
        self.assertEquals(find_closest_intersection("R75,D30,R83,U83,L12,D49,R71,U7,L72",
                                                    "U62,R66,U55,R34,D71,R55,D58,R83"), 159)
        self.assertEquals(find_closest_intersection("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
                                                    "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"), 135)

if __name__ == '__main__':
    unittest.main()
