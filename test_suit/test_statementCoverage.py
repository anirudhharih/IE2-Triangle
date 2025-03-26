import unittest
from isTriangle import Triangle


class TestStatementCoverage(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(Triangle.classify(3, 3, 3), Triangle.Type.EQUILATERAL)

    def test_scalene(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)

    def test_isosceles_1(self):
        self.assertEqual(Triangle.classify(3, 3, 4), Triangle.Type.ISOSCELES)

    def test_isosceles_2(self):
        self.assertEqual(Triangle.classify(3, 4, 3), Triangle.Type.ISOSCELES)

    def test_isosceles_3(self):
        self.assertEqual(Triangle.classify(4, 3, 3), Triangle.Type.ISOSCELES)

    def test_invalid_negative(self):
        self.assertEqual(Triangle.classify(-1, 3, 3), Triangle.Type.INVALID)

    def test_invalid_zero(self):
        self.assertEqual(Triangle.classify(0, 3, 3), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_1(self):
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_2(self):
        self.assertEqual(Triangle.classify(2, 1, 3), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_3(self):
        self.assertEqual(Triangle.classify(2, 3, 1), Triangle.Type.INVALID)


if __name__ == "__main__":
    unittest.main()
