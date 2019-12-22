"""
Module to test the day 1 code.
"""

import unittest
from calculate_fuel_from_mass import read_mass_from_file
from calculate_fuel_from_mass import calculate_fuel_from_mass
from calculate_fuel_from_mass import calculate_total_fuel

class Tests(unittest.TestCase):
    """Class which contains unit tests for day 1 code.

    """
    def test_calculate_fuel_from_mass(self):
        """Tests calculate_fuel_from_mass with provided sample values.

        """
        self.assertEqual(calculate_fuel_from_mass(12), 2)
        self.assertEqual(calculate_fuel_from_mass(14), 2)
        self.assertEqual(calculate_fuel_from_mass(1969), 654)
        self.assertEqual(calculate_fuel_from_mass(100756), 33583)

    def test_get_masses_from_file(self):
        """Tests read_mass_from_file with a short sample file test_input.txt.

        """
        self.assertEqual(read_mass_from_file("test_input.txt"), [1345, 235, 12, 456, 45])

    def test_calculate_total_fuel(self):
        """Tests readMassFromFile with a short sample file test_input.txt.

        """
        self.assertEqual(calculate_total_fuel("test_input.txt"), 687)

if __name__ == '__main__':
    unittest.main()
