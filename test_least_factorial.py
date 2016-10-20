import unittest
import least_factorial as T

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(T.least_factorial(1), 1)
        self.assertEqual(T.least_factorial(2), 2)
        self.assertEqual(T.least_factorial(3), 6)
        self.assertEqual(T.least_factorial(5), 6)
        self.assertEqual(T.least_factorial(17), 24)
        self.assertEqual(T.least_factorial(42), 120)
        self.assertEqual(T.least_factorial(120), 120)
        self.assertEqual(T.least_factorial(121), 720)

        self.assertEqual(T.least_factorial(1000), 5040)

        self.assertEqual(T.least_factorial(0), 1)

if __name__ == '__main__':
    unittest.main()
