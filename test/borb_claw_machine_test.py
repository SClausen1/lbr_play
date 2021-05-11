from cheats import borb_claw_machine
import unittest
import cv2

class TestBorbClawMachine(unittest.TestCase):

    def setUp(self):        
        self.screenshot =cv2.imread('test\data\game_no_curse.png')

    
    def test_identify_curse(self):
        x, y =borb_claw_machine.find_curse(self.screenshot)
        self.assertAlmostEqual(y, 437) 
        self.assertAlmostEqual(x, 819) 
    
    
    #@unittest.skip("change img.pixel(x,y) to img[x,y]")
    def test_operate_claw(self):
        self.assertEqual(borb_claw_machine.operate_claw(20, self.screenshot), True)



    @unittest.skip("For getting mouse x,y")
    def test_get_mouse_location(self):
        import mouse
        print('left click to print mouse position')
        mouse.wait('left')
        print(mouse.get_position())
