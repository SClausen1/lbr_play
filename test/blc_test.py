import mss
import unittest
from cheats.blc_time_travel import *
from PIL import Image

class BLCTimeTravelTest(unittest.TestCase):
    def setUp(self):        
        self.screenshot = Image.open(r'test\data\test_image_font_2.png')
        self.inverted_img = invert_screenshot(self.screenshot)
        self.text = pytesseract.image_to_string(self.inverted_img)
        self.time_dict = extract_relevant_text(self.text)
        self.seconds = dict_to_seconds(self.time_dict)

        
    def test_extract_text(self):
        self.assertEqual(self.time_dict, {'days': 458, 'hours': 8, 'minutes': 21, 'seconds': 30})

    def test_dict_to_seconds(self):   
        self.assertEqual(self.seconds, 458*24*60*60 + 8*60*60 + 21*60 + 30 -1)


    @unittest.skip("find desired moniter size utility")
    def test_show_moniter_size(self):
        time.sleep(2)
        with mss.mss() as sct:
            monitor = {"top": 205, "left": 290, "width": 1200, "height": 640}
            cv2.imshow("Image", np.array(sct.grab(monitor)))
        while True:
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
