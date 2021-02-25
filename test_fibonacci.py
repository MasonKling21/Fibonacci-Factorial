import unittest
from fibonacci import *

class TestFibonacciSeq(unittest.TestCase):
    def test_seq(self):
        self.assertEqual((fibonacci(1)), 0)
        self.assertEqual((fibonacci(2)), 1)
        self.assertEqual((fibonacci(3)), 1)
        self.assertEqual((fibonacci(4)), 2)
        self.assertEqual((fibonacci(5)), 3)
        self.assertEqual((fibonacci(6)), 5)
        self.assertEqual((fibonacci(7)), 8)
        self.assertEqual((fibonacci(8)), 13)

    def test_fib(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

def test_answer():
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(8) == 13
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


if __name__ == "__main__":
    unittest.main()
