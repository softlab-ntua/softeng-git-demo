import unittest
import fib as T

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(T.fib(0), 0)
        self.assertEqual(T.fib(1), 1)
        self.assertEqual(T.fib(2), 1)
        self.assertEqual(T.fib(3), 2)
        self.assertEqual(T.fib(4), 3)
        self.assertEqual(T.fib(5), 5)
        self.assertEqual(T.fib(6), 8)

if __name__ == '__main__':
    unittest.main()
