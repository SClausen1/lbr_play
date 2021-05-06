import unittest
from helpers import set_time
from _datetime import datetime, timedelta

class TestWinSetTime(unittest.TestCase):
    def test_5_min(self):
        self.assertEqual( set_time.calculate_time(300).minute, (datetime.now().minute + 5) % 60)
        
    def test_1_hour(self):
        self.assertEqual(set_time.calculate_time(3600).hour, datetime.now().hour + 1)
        hour_future = datetime.now() + timedelta(3600)

        self.assertEqual(set_time.calculate_time(3600).hour, hour_future.hour)


if __name__ == '__main__':
    unittest.main()