import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(0,0),0)
    
    def test_subtract(self):
        self.assertEqual(subtract(5,3),2)
        self.assertEqual(subtract(0,4),-4)
        self.assertEqual(subtract(-2,-2),0)


    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2,3),6)
        self.assertEqual(mul(-1,5),-5)
        self.assertEqual(mul(0,10),0)

    def test_divide(self):
        self.assertEqual(div(6,3),2)
        self.assertEqual(div(5,2),2.5)
        self.assertEqual(div(-6,2),-3)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5,0)

    def test_logarithm(self):
        self.assertEqual(logarithm(8,2),3)
        self.assertEqual(logarithm(100,10),2)
        self.assertEqual(logarithm(1,10),0)
 

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10,1)

    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0,10)
   

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(8,15),17)
 

    def test_sqrt(self):
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(9),3)
        self.assertEqual(square_root(0),0)
    

# Do not touch this
if __name__ == "__main__":
    unittest.main()
