import unittest
import cheats.faster_crunch as fc
import time

class TestFasterCrunch(unittest.TestCase):
    
    @unittest.skip("manual test case")
    def test_buy_crunch_macro(self):
        print('buy and crunch test in 3')
        time.sleep(3)
        fc.buy_and_crunch_macro()