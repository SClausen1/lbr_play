
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


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'




with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 40, "left": 0, "width": 1500, "height": 800}

    while "Screen capturing":
        

        # Get raw pixels from the screen, save it to a Numpy array
        print('Grabbing screen in 5')
        time.sleep(5)   
        img = np.array(sct.grab(monitor))
        greyscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inverted_img = cv2.bitwise_not(greyscale_img)
        cv2.imshow("Image", inverted_img)
        # Display the picture
        text = pytesseract.image_to_string(inverted_img)
        lines = text.splitlines()
        try:
            index = lines.index("Orb of ELC fon")
        except ValueError:
            print(text)
            break
        
        line = lines[index + 2].split
        print(line)
        time = line[line.index('in')+1:]
        timeDict = {}
        time_remaining = 0

        for i in range(len(time), step=2):
            timeDict[time[i+1]] = time[i]

        for key in timeDict.keys:
            if key == 'seconds':
                time_remaining += int(timeDict.get(key))
            elif key =='hours':
                time_remaining += int(timeDict.get(key)) * 3600
            elif key == 'minutes':
                time_remaining += int(timeDict.get(key)) * 60
            else:
                time_remaining += int(timeDict.get(key)) * 3600 * 24
        time_desired = time.time() + time_remaining
        time.localtime(time_desired)
        print(text)
        break
        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

