import sys
import os
from unittest import TestCase, main

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from main import Triangle


class TriangleTest(TestCase):

    def test_int(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area, 6.0)
    
    def test_degeneracy(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(1, 2, 3)
    
    def test_float(self):
        triangle = Triangle(3.1, 4.5, 5.1)
        self.assertEqual(triangle.area, 6.908271762894102)

    def test_is_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

    def test_is_not_right(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right())
    
    def test_nothing(self):
        with self.assertRaises(TypeError):
            triangle = Triangle()
    
    def test_negative(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(-1, 0, 1)

    def test_string(self):
        with self.assertRaises(TypeError):
            triangle = Triangle("1", 2, 3)

    def test_list(self):
        with self.assertRaises(TypeError):
            triangle = Triangle([1,2,3], [1,2,3], [1,2,3])

    def test_dict(self):
        with self.assertRaises(TypeError):
            triangle = Triangle({1: 2, 3: 4, 5: 6})

    def test_zero(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(0, 0, 0)

    def test_bool(self):
        with self.assertRaises(TypeError):
            triangle = Triangle(True, False, True)

            
if __name__ == "__main__":
    main()