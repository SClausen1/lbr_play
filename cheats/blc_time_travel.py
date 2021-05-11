import numpy as np
import cv2
import mss
import threading
from helpers import set_time,text_from_menu
import keyboard
import time


def main_loop():

    click_listener_thread = threading.Thread(target=keyboard.wait, args=('enter',))
    print('press enter to stop BLC Time Travl')
    click_listener_thread.start()
    print('Grabbing screen in 5')
    time.sleep(5) 
    while click_listener_thread.is_alive():
        time_travel()
        time.sleep(5)
    return 1
     

def time_travel():

            
    screenshot_words = get_text_from_menu()
    time_dict = extract_relevant_text(screenshot_words)
    if(time_dict == None):
        print("time travel failed")
        return
    seconds = dict_to_seconds(time_dict)
    print('moving forward {} seconds'.format(seconds))
    set_time._win_set_time(seconds)

    

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
    return time_remaining - 1

def extract_relevant_text(text):
    lines = text.splitlines()
    for line in lines:
        if line.startswith('Orb of BLC'):

            index = lines.index(line) 
            try: 
                if len(lines[index + 3].split('Spawned')) > 1:
                    break
                time_line = lines[index + 3].split(' in')[2].strip('.').split()
                time_dict = {}
                for i in range(0,len(time_line),2):
                    time_dict[time_line[i+1]] = int(time_line[i])
                return time_dict
            except(IndexError, ValueError):
                pass
            
    return None




def get_name():
    return "BLC Time Travel"