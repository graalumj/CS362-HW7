# test_FizzBuzz.py
# By Alex Graalum
import unittest
import FizzBuzz

class test_FizzBuzz(unittest.TestCase):
    def test_three(self):
        self.assertEqual(FizzBuzz.fizzbuzz(9), "Fizz")
    def test_five(self):
        self.assertEqual(FizzBuzz.fizzbuzz(20), "Buzz")
    
if __name__ == '__main__':
    unittest.main()

