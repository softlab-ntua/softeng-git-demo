import unittest
import gcd as T

from hypothesis import given, assume
from hypothesis.strategies import integers

class Test(unittest.TestCase):

    @given(integers(min_value=0), integers(min_value=0))
    def test_hypothesis(self, a, b):
        assume(a + b > 0)
        g = T.gcd(a, b)
        assert isinstance(g, int)
        assert g >= 1
        assert a % g == 0
        assert b % g == 0
        # Skip very long tests...
        if min(a, b) // g > 1000000: return
        assert all(a % k != 0 or b % k != 0 for k in range(2*g, min(a, b)+1, g))

if __name__ == '__main__':
    unittest.main()
