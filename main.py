import sys
sys.path.append('C:\\Users\\The Heart of Gold\\lbr_play')
from cheats import auto_leaf_keeper, blc_time_travel, cheese_grind, faster_crunch, borb_claw_machine
from helpers import set_time, capture_mouse

import keyboard  

import time

semaphore = 1
scripts = {
    '1' : auto_leaf_keeper,
    '2' : blc_time_travel,
    '3' : cheese_grind,
    '4' : faster_crunch,
    '5' : borb_claw_machine,

    '0' : capture_mouse
}

def event_scheduler(keyboard_event):
    if keyboard_event.name == 'esc':
        semaphore = -1
    elif scripts.get(keyboard_event.name) == None:
        print("Invalid Entry")
    else:
        semaphore = scripts[keyboard_event.name].main_loop()
 

        
if __name__=="__main__":

    while True:
        if semaphore > 0 :
            for k,v in scripts.items():
                print('press ' + k + ' for ' + v.get_name())
            print('press esc to quit')
            semaphore = 0
            keyboard.hook(event_scheduler) 
        elif semaphore == 0:
            time.sleep(1)
        else:
            print("Goodbye!")
            break
        


