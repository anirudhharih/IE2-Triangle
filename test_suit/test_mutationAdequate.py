import unittest
from isTriangle import Triangle


class TestMutationAdequate(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(Triangle.classify(10, 10, 10), Triangle.Type.EQUILATERAL)

    def test_scalene(self):
        self.assertEqual(Triangle.classify(7, 9, 12), Triangle.Type.SCALENE)

    def test_isosceles_1(self):
        self.assertEqual(Triangle.classify(5, 5, 9), Triangle.Type.ISOSCELES)

    def test_isosceles_2(self):
        self.assertEqual(Triangle.classify(9, 5, 5), Triangle.Type.ISOSCELES)

    def test_isosceles_3(self):
        self.assertEqual(Triangle.classify(5, 9, 5), Triangle.Type.ISOSCELES)

    def test_invalid_negative(self):
        self.assertEqual(Triangle.classify(-2, 5, 5), Triangle.Type.INVALID)

    def test_invalid_zero(self):
        self.assertEqual(Triangle.classify(0, 5, 5), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_1(self):
        self.assertEqual(Triangle.classify(2, 2, 5), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_2(self):
        self.assertEqual(Triangle.classify(2, 5, 2), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_3(self):
        self.assertEqual(Triangle.classify(5, 2, 2), Triangle.Type.INVALID)


if __name__ == "__main__":
    unittest.main()
