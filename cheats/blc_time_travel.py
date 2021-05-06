import pytesseract
import numpy as np
import cv2
import mss
import threading
from helpers import set_time
import keyboard
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def main_loop():
    click_listener_thread = threading.Thread(target=keyboard.wait, args=('enter'))
    print('press enter to stop BLC Time Travl')
    click_listener_thread.start()
    
    while click_listener_thread.is_alive():
        time_travel()
     

def time_travel():
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": 205, "left": 290, "width": 1200, "height": 640}

        # Get raw pixels from the screen, save it to a Numpy array
        print('Grabbing screen in 5')
        time.sleep(5)   
        # invert image, to get black text
        print('Inverting image')
        inverted_img = invert_screenshot(sct.grab(monitor))
        print('Extracting Text')
        time_dict = extract_relevant_text(pytesseract.image_to_string(inverted_img))
        if(time_dict == None):
            print("time travel failed")
            return
        seconds = dict_to_seconds(time_dict)
        print('moving forward {} seconds'.format(seconds))
        set_time._win_set_time(seconds)
        time.sleep(20)
  

def dict_to_seconds(time_dict):
    time_remaining = 0
    if time_dict:
        for key in time_dict.keys():
                if key == 'seconds':
                    time_remaining += time_dict.get(key)
                elif key =='hours':
                    time_remaining += time_dict.get(key) * 3600
                elif key == 'minutes':
                    time_remaining += time_dict.get(key) * 60
                else:
                    time_remaining += time_dict.get(key) * 3600 * 24
    return time_remaining

def extract_relevant_text(text):
    lines = text.splitlines()
    for line in lines:
        if line.startswith('Orb of BLC'):
            index = lines.index(line)  
            time_line = lines[index + 3].split(' in')[2].strip('.').split()
            time_dict = {}
            for i in range(0,len(time_line),2):
                time_dict[time_line[i+1]] = int(time_line[i])
            return time_dict
            
    return None


def invert_screenshot(screensthot):
    img = np.array(screensthot)
    greyscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_img = cv2.bitwise_not(greyscale_img)
    return inverted_img