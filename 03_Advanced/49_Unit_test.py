import unittest

##This functional is a part of another file factorial.py
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

##This is part of test_factorial.py , which python understand as unittest.

class TestFactorial(unittest.TestCase):


   def test_factorial_of_0(self):
       self.assertEqual(factorial(0), 1)


   def test_factorial_of_positive_number(self):
       self.assertEqual(factorial(5), 120)
       self.assertEqual(factorial(10), 3628800)


   def test_factorial_of_negative_number(self):
       with self.assertRaises(ValueError):
           factorial(-1)


if __name__ == '__main__':
   unittest.main()
