import unittest
from model import Vector2d, MoveDirection

class TestVector2d(unittest.TestCase):

    def test_addition(self):
        v1 = Vector2d(1, 2)
        v2 = Vector2d(3, 4)
        result = v1.add(v2)
        self.assertEqual(result, Vector2d(4, 6))

    def test_subtraction(self):
        v1 = Vector2d(5, 6)
        v2 = Vector2d(2, 2)
        result = v1.subtract(v2)
        self.assertEqual(result, Vector2d(3, 4))

    def test_upper_right(self):
        v1 = Vector2d(2, 4)
        v2 = Vector2d(3, 1)
        result = v1.upperRight(v2)
        self.assertEqual(result, Vector2d(3, 4))

    def test_lower_left(self):
        v1 = Vector2d(2, 4)
        v2 = Vector2d(3, 1)
        result = v1.lowerLeft(v2)
        self.assertEqual(result, Vector2d(2, 1))

    def test_opposite(self):
        v = Vector2d(2, -3)
        result = v.opposite()
        self.assertEqual(result, Vector2d(-2, 3))

if __name__ == '__main__':
    unittest.main()