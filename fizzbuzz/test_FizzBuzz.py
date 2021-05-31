# test_FizzBuzz.py
# By Alex Graalum
import unittest
import FizzBuzz

class test_FizzBuzz(unittest.TestCase):
    def test_three(self):
        self.assertEqual(FizzBuzz.fizzbuzz(9), "Fizz")
    
if __name__ == '__main__':
    unittest.main()

