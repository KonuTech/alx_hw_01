import unittest

from scripts.shapes import Circle, Square


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(5)

    def test_circle_area(self):
        # Test area calculation for Circle class
        expected_area = 78.54
        self.assertAlmostEqual(self.circle.area, expected_area, places=2)

    def test_circle_properties_non_negative(self):
        # Test properties (area, radius, diameter) for
        # non-negativity in Circle class
        self.assertGreaterEqual(self.circle.area, 0)
        self.assertGreaterEqual(self.circle.radius, 0)
        self.assertGreaterEqual(self.circle.diameter, 0)


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(5)

    def test_square_properties_non_negative(self):
        # Test properties (area, side) for non-negativity
        # in Square class
        self.assertGreaterEqual(self.square.area, 0)
        self.assertGreaterEqual(self.square.side, 0)

    def test_square_area(self):
        # Test area calculation for Square class
        expected_area = 25
        self.assertEqual(self.square.area, expected_area)

    # Add more test cases as needed to cover various
    # functionalities of the Square class


if __name__ == "__main__":
    unittest.main()
