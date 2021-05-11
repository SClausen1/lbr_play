import cv2
import pytesseract
import mss


def get():
    with mss.mss() as sct:
        # capture just menu for cleaner image
        monitor = {"top": 205, "left": 290, "width": 1200, "height": 640}
        inverted_img = invert_screenshot(sct.grab(monitor))
        return pytesseract.image_to_string(inverted_img)

def invert_screenshot(screensthot):
    img = np.array(screensthot)
    greyscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_img = cv2.bitwise_not(greyscale_img)
    return inverted_img