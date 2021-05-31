# test_LeapYear.py
# By Alex Graalum
import unittest
import LeapYear

class test_leapyear(unittest.TestCase):
    def test_four(self):
        self.assertEqual(LeapYear.leapyear(2012), true)
    def test_hundred(self):
        self.assertEqual(LeapYear.leapyear(2100), false)
    def test_fourhundred(self):
        self.assertEqual(LeapYear.leapyear(2000), true)
    def test_normal(self):
        self.assertEqual(LeapYear.leapyear(2002), false)
    
if __name__ == '__main__':
    unittest.main()
    
