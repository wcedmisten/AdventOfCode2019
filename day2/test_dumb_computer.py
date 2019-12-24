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
        big provided example.

        """
        computer = DumbComputer("1,9,10,3,2,3,11,0,99,30,40,50")
        self.assertEqual(computer.process_instructions(),
                            "3500,9,10,70,2,3,11,0,99,30,40,50")

    def test_first_small_example(self):
        """Tests the DumbComputer.process_instructions function with the
        first small example.

        """
        computer = DumbComputer("1,0,0,0,99")
        self.assertEqual(computer.process_instructions(), "2,0,0,0,99")

    def test_second_small_example(self):
        """Tests the DumbComputer.process_instructions function with the
        second small example.

        """
        computer = DumbComputer("2,3,0,3,99")
        self.assertEqual(computer.process_instructions(), "2,3,0,6,99")

    def test_third_small_example(self):
        """Tests the DumbComputer.process_instructions function with the
        third small example.

        """
        computer = DumbComputer("2,4,4,5,99,0")
        self.assertEqual(computer.process_instructions(), "2,4,4,5,99,9801")

    def test_fourth_small_example(self):
        """Tests the DumbComputer.process_instructions function with the
        fourth small example.

        """
        computer = DumbComputer("1,1,1,4,99,5,6,0,99")
        self.assertEqual(computer.process_instructions(), "30,1,1,4,2,5,6,0,99")


if __name__ == '__main__':
    unittest.main()
