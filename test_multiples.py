import unittest
import mathFunctions

class TestMathFunctions(unittest.TestCase):
    def test_multiples(self):
        result = mathFunctions.multiples()
        self.assertEqual(result, 51)

    def test_add(self):
        self.assertEqual(mathFunctions.add(5,7), 12)
        self.assertEqual(mathFunctions.add(-1,1),0)
        self.assertEqual(mathFunctions.add(-1,-1),-2)

    def test_sub(self):
        self.assertEqual(mathFunctions.subtract(7,5), 2)
        self.assertEqual(mathFunctions.subtract(-1,1),-2)
        self.assertEqual(mathFunctions.subtract(-1,-1),0)

    def test_multiply(self):
        self.assertEqual(mathFunctions.multiply(5,7), 35)
        self.assertEqual(mathFunctions.multiply(-1,0),0)
        self.assertEqual(mathFunctions.multiply(-1,-1),1)

    def test_divide(self):
        self.assertEqual(mathFunctions.division(10,5), 2)
        self.assertEqual(mathFunctions.division(-1,1),-1)
        self.assertEqual(mathFunctions.division(-1,-1),1)
        self.assertEqual(mathFunctions.division(5,2),2.5)

        # self.assertRaises(ValueError, mathFunctions.division, 5,0)
        # or
        with self.assertRaises(ValueError):
            mathFunctions.division(5,0)

if __name__ == '__main__':
    unittest.main()
