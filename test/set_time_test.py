import unittest
from helpers import set_time
from _datetime import datetime

class TestWinSetTime(unittest.TestCase):
    def test_5_min(self):
        time = set_time.calculate_time(300)
        self.assertEqual(len(time), 8)
        self.assertEqual(time[5], datetime.now().minute + 5)
        
    def test_1_hour(self):
        self.assertEqual(set_time.calculate_time(3600)[4], datetime.now().hour + 1)


if __name__ == '__main__':
    unittest.main()