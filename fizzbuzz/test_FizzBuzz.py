# test_FizzBuzz.py
# By Alex Graalum
import unittest
import FizzBuzz

class test_FizzBuzz(unittest.TestCase):
    def test_three(self):
        self.assertEqual(FizzBuzz.fizzbuzz(9), "Fizz")
    def test_five(self):
        self.assertEqual(FizzBuzz.fizzbuzz(20), "Buzz")
    def test_fifteen(self):
        self.assertEqual(FizzBuzz.fizzbuzz(45), "FizzBuzz")
    
if __name__ == '__main__':
    unittest.main()

