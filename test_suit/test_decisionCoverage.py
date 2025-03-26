import unittest
from isTriangle import Triangle


class TestDecisionCoverage(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(Triangle.classify(5, 5, 5), Triangle.Type.EQUILATERAL)

    def test_scalene(self):
        self.assertEqual(Triangle.classify(6, 8, 10), Triangle.Type.SCALENE)

    def test_isosceles_1(self):
        self.assertEqual(Triangle.classify(5, 5, 7), Triangle.Type.ISOSCELES)

    def test_isosceles_2(self):
        self.assertEqual(Triangle.classify(7, 5, 5), Triangle.Type.ISOSCELES)

    def test_isosceles_3(self):
        self.assertEqual(Triangle.classify(5, 7, 5), Triangle.Type.ISOSCELES)

    def test_invalid_negative(self):
        self.assertEqual(Triangle.classify(-5, 4, 4), Triangle.Type.INVALID)

    def test_invalid_zero(self):
        self.assertEqual(Triangle.classify(0, 4, 4), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_1(self):
        self.assertEqual(Triangle.classify(1, 2, 4), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_2(self):
        self.assertEqual(Triangle.classify(2, 4, 1), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_3(self):
        self.assertEqual(Triangle.classify(4, 1, 2), Triangle.Type.INVALID)


if __name__ == "__main__":
    unittest.main()
