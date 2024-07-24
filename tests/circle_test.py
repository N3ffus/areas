import sys
import os
from unittest import TestCase, main

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from main import Circle


class CircleTest(TestCase):

    def test_int(self):
        circle = Circle(5)
        self.assertEqual(circle.area, 78.53981633974483)
    
    def test_float(self):
        circle = Circle(2.5)
        self.assertEqual(circle.area, 19.634954084936208)

    def test_negative_int(self):
        with self.assertRaises(ValueError):
            circle = Circle(-5)

    def test_negative_float(self):
        with self.assertRaises(ValueError):
            circle = Circle(-10.52)

    def test_zero(self):
        with self.assertRaises(ValueError):
            circle = Circle(0)

    def test_string(self):
        with self.assertRaises(TypeError):
            circle = Circle("5")

    def test_bool(self):
        with self.assertRaises(TypeError):
            circle = Circle(True)
    
    def test_dict(self):
        with self.assertRaises(TypeError):
            circle = Circle({5: 12})

    def test_list(self):
        with self.assertRaises(TypeError):
            circle = Circle([1,2,3])
    
    def test_nothing(self):
        with self.assertRaises(TypeError):
            circle = Circle()


            
if __name__ == "__main__":
    main()