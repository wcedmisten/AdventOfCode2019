import unittest
from calculateFuelFromMass import *

class Tests(unittest.TestCase):
    def test_calculate_fuel_from_mass(self):
        self.assertEqual(calculateFuelFromMass(12), 2)
        self.assertEqual(calculateFuelFromMass(14), 2)
        self.assertEqual(calculateFuelFromMass(1969), 654)
        self.assertEqual(calculateFuelFromMass(100756), 33583)

if __name__ == '__main__':
    unittest.main()
