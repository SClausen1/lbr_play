import mouse
import os
import pickle

def main_loop():
    record = mouse_script()
    record_name = ""
    print('What cheat is this for?\n1 for Auto Leaf Keaper \n2 for BLC Time Hacker\n3 for Cheese Grind\n:')
    cheat = input('What cheat is this for?\n1 for Auto Leaf Keaper \n2 for BLC Time Hacker\n3 for Cheese Grind\n: ')
    
    if cheat == '1':
        record_name = "recordings/auto_leaf_keeper.pkl"
    elif cheat == '2':
        record_name = "recordings/blc_time_hacker.pkl"
    elif cheat == '3':
        record_name = "recordings/cheese_grind.pkl"
    else:
        print(cheat + ' is an invalid input')

    with open(record_name, 'wb') as output:
        pickle.dump(record, output, pickle.HIGHEST_PROTOCOL)
    return 1
    
def get_name():
    return "Capture Mouse"
# def record_namer(keyboard_event):
#     record_name = ""

#     if keyboard_event.name == '1':
#         record_name = "auto_leaf_keeper.pkl"
#     elif keyboard_event.name == '2':
#         record_name = "blc_time_hacker.pkl"
#     elif keyboard_event.name == '3':
#         record_name = "cheese_grind.pk1"
1
#     return record_name

def mouse_script():
    print("Right click to start and stop recording your mouse")

    mouse.wait('right')
    
    print("recording...")

    record = mouse.record(button='right')

    print("recording finished")

    return record
