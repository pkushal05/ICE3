# Name: Kushal Patel
# Date: 5th March 2025
# Title: ICE3 (Temperature sensors)
# Desc: This is the testcases for ICE3

from src.program import validate_temp, process_temp
import unittest

class TestTemperatureFunctions(unittest.TestCase):

    def test_validate_temp_min(self):
        self.assertEqual(validate_temp([-50]), [-50])

    def test_validate_temp_max(self):
        self.assertEqual(validate_temp([150]), [150])

    def test_validate_temp_near_boundary(self):
        self.assertEqual(validate_temp([-49, 149]), [-49, 149])

    def test_validate_temp_mixed(self):
        with self.assertRaises(ValueError):
            validate_temp([20, -60, 160])

    def test_validate_temp_alp_char(self):
        with self.assertRaises(ValueError):
            validate_temp([20, "abc", 30])

    def test_validate_temp_invalid_input(self):
        with self.assertRaises(ValueError):
            validate_temp([10, "@", -40])

    def test_validate_temp_very_large(self):
        with self.assertRaises(ValueError):
            validate_temp([2**31, -1, -2**31])

    def test_validate_temp_all_same(self):
        self.assertEqual(validate_temp([50, 50, 50]), [50, 50,50])

    def test_validate_empty(self):
        self.assertEqual(validate_temp([]), "No input provided!")

    def test_process_temp_valid_list(self):
        self.assertEqual(process_temp([10, 20, 30]), "Min: 10°C, Max: 30°C, Avg: 20.0°C")

    def test_process_temp_empty_list(self):
        self.assertEqual(process_temp([]), "No input provided!")

if __name__ == '__main__':
    unittest.main()