"""
Module to test the day 2 code.
"""

import unittest
from dumb_computer import DumbComputer

class Tests(unittest.TestCase):
    """Class which contains unit tests for day 2 code.

    """
    def test_big_example(self):
        """Tests the DumbComputer.process_instructions function with the
        big provided example

        """
        computer = DumbComputer("1,9,10,3,2,3,11,0,99,30,40,50")
        self.assertEqual(computer.process_instructions(),
                            "3500,9,10,70,2,3,11,0,99,30,40,50")



if __name__ == '__main__':
    unittest.main()
