import unittest

from scripts.figure import Circle, Square, Triangle


class TestSquare(unittest.TestCase):
    def test_square_area(self):
        s = Square(5)
        self.assertEqual(s.area, 25)

    def test_square_perimeter(self):
        s = Square(5)
        self.assertEqual(s.perimeter(), 20)

    def test_square_comparison(self):
        s1 = Square(4)
        s2 = Square(5)
        self.assertTrue(s1 < s2)
        self.assertFalse(s2 < s1)

    def test_square_addition(self):
        s1 = Square(4)
        s2 = Square(5)
        s3 = s1.area + s2.area
        self.assertEqual(s3, 41)


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area, 78.54, places=2)

    def test_circle_perimeter(self):
        c = Circle(5)
        self.assertAlmostEqual(c.perimeter(), 31.42, places=2)

    def test_circle_comparison(self):
        c1 = Circle(4)
        c2 = Circle(5)
        self.assertTrue(c1 < c2)
        self.assertFalse(c2 < c1)

    def test_circle_addition(self):
        c1 = Circle(4)
        c2 = Circle(5)
        c3 = c1.area + c2.area
        self.assertAlmostEqual(c3, (50.2655 + 78.5398), places=2)


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        t = Triangle(4, 5)
        self.assertEqual(t.area, 10)

    def test_triangle_perimeter(self):
        t = Triangle(4, 5)
        self.assertEqual(t.perimeter(), 12)

    def test_triangle_comparison(self):
        t1 = Triangle(3, 4)
        t2 = Triangle(4, 5)
        self.assertTrue(t1 < t2)
        self.assertFalse(t2 < t1)


if __name__ == "__main__":
    unittest.main()
