# Plik test_model.py

import unittest
from model import Vector2d, MoveDirection
from controller import OptionsParser

class TestOptionsParser(unittest.TestCase):

    def test_parse(self):
        # Test prawidłowych kierunków
        args = ["FORWARD", "LEFT", "BACKWARD", "RIGHT"]
        result = OptionsParser.parse(args)
        expected = [MoveDirection.FORWARD, MoveDirection.LEFT, MoveDirection.BACKWARD, MoveDirection.RIGHT]
        self.assertEqual(result, expected)

    def test_parse_invalid_directions(self):
        # Test nieprawidłowych kierunków, które powinny zostać zignorowane
        args = ["FORWARD", "INVALID", "LEFT", "INVALID", "BACKWARD"]
        result = OptionsParser.parse(args)
        expected = [MoveDirection.FORWARD, MoveDirection.LEFT, MoveDirection.BACKWARD]
        self.assertEqual(result, expected)

    def test_parse_empty_args(self):
        # Test braku argumentów
        args = []
        result = OptionsParser.parse(args)
        expected = []
        self.assertEqual(result, expected)

    def test_parse_mixed_case(self):
        # Test mieszanych przypadków wielkości liter 
        args = ["forward", "LEfT", "BaCkWaRd", "riGHT"]
        result = OptionsParser.parse(args)
        expected = []
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
