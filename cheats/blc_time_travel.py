
import pytesseract



import numpy as np
import cv2
from PIL import ImageGrab, Image
import mss
import os
import os.path
import time

import requests
from urllib.request import urlopen
from helpers import set_time

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
        monitor = {"top": 40, "left": 0, "width": 1500, "height": 800}

        while "Screen capturing":
            

            # Get raw pixels from the screen, save it to a Numpy array
            print('Grabbing screen in {}' 5)
            time.sleep(5)   
            # invert image, to get black text
            inverted_img = invert_screenshot(sct.grab(monitor))
        
            time_dict = extract_relevant_text(pytesseract.image_to_string(inverted_img))

            seconds = dict_to_seconds
            
            set_time._win_set_time(seconds)
            time.sleep(20)
  

def dict_to_seconds(time_dict)
    for key in time_dicts.keys:
            if key == 'seconds':
                time_remaining += int(time_dicts.get(key))
            elif key =='hours':
                time_remaining += int(time_dicts.get(key)) * 3600
            elif key == 'minutes':
                time_remaining += int(time_dicts.get(key)) * 60
            else:
                time_remaining += int(time_dicts.get(key)) * 3600 * 24

def extract_relevant_text(lines)
    lines = text.splitlines()
    try:
        index = lines.index("Orb of ELC fon")
    except ValueError:
        print(text)
        break
    
    line = lines[index + 2].split
    print(line)
    time = line[line.index('in')+1:]
    time_dict = {}
    time_remaining = 0

    for i in range(len(time), step=2):
        time_dict[time[i+1]] = time[i]
    return time_dict

def invert_screenshot(screensthot):
    img = np.array(screensthot))
    greyscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_img = cv2.bitwise_not(greyscale_img)
    cv2.imshow("Image", inverted_img)