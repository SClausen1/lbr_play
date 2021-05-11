import unittest
from helpers import set_time
from _datetime import datetime, timedelta
import win32api
import ctypes, os
class TestWinSetTime(unittest.TestCase):
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    def test_5_min(self):
        local_time = datetime.utcnow()
        time = set_time.calculate_time(300)
        self.assertEqual(time.minute ,( local_time.minute + 5))
        self.assertEqual(time.hour, local_time.hour)
    def test_1_hour(self):
        self.assertEqual(set_time.calculate_time(3600).hour, datetime.utcnow().hour + 1)
        self.assertEqual(set_time.calculate_time(3600).minute, datetime.utcnow().minute)
    
    @unittest.skipUnless(is_admin, "Test requires admin privlages")
    def test_1_min(self):
        local_time =  win32api.GetLocalTime()
        set_time._win_set_time(60)
        local_time2 = win32api.GetLocalTime()
        #print('Time 1: ' +str(local_time) + '\nTime 2' + str(local_time2))
        self.assertEqual(local_time[5] + 1, local_time2[5])

if __name__ == '__main__':
    unittest.main()