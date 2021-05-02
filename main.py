from auto-leaf-keaper import mouse_script

import keyboard      

def event_scheduler(keyboard_event):
    if keyboard_event['name'] == 'esc':
        return True
    elif keyboard_event['name'] == '1':
        mouse_script()
    elif keyboard_event['name'] == '2':
        blc-time-travel()

        
if __name__=="__main__":
    while True
        print("press 1 for auto-leaf-keaper 2 for BLC time hacker and esc to quit")
        keyboard_input = keyboard.hook()
        esc = False
        while not esc:
            esc = keyboard.hook(event_scheduler)

