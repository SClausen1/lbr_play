import sys
sys.path.append('C:\\Users\\The Heart of Gold\\lbr_play')
from cheats import auto_leaf_keeper, blc_time_travel, cheese_grind
from helpers import set_time, capture_mouse

import keyboard  

import time

semaphore = 1

def event_scheduler(keyboard_event):
    if keyboard_event.name == 'esc':
        semaphore = -1
        return
    elif keyboard_event.name == '1':
        auto_leaf_keeper.main_loop()
    elif keyboard_event.name == '2':
        blc_time_travel.main_loop()
    elif keyboard_event.name == '3':
        cheese_grind.mouse_script()
    elif keyboard_event.name == '4':
        capture_mouse.main_script()
    semaphore = 1
    return

        
if __name__=="__main__":

    while True:
        if semaaphore > 0 :
            print('''1 for Auto Leaf Keaper \n2 for BLC Time Hacker \n3 for Cheese Grind\
                    \n4 for Mouse Capture Util \nesc to quit''')
            semaphore = 0
            keyboard.hook(event_scheduler) 
        elif semaphore == 0:
            time.sleep(1)
        else:
            print("Goodbye!")
            break
        


