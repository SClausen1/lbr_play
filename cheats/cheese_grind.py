import mouse 
import threading 
import sys

from helpers.set_time import _win_set_time
from helpers import text_from_menu
import keyboard


def mouse_mover(record):
    while True:
        mouse.play(record)

def main_loop():
    with open("recordings/auto_leaf_keaper.pkl", 'rb') as input:
        record = pickle.load(input)
    click_listener_thread = threading.Thread(target=keyboard.wait, args=('enter',))
    print('press enter to stop cheese grind')
    click_listener_thread.start()
    time.sleep(3)
    while click_listener_thread.is_alive():
        #collect
        mouse.play(record, speed_factor=1)
        #wait 3 min
        _win_set_time(60*3)

        #buy new 
        mouse.play(record, speed_factor=1)
        #wait 2 hours
        _win_set_time(2*3600)

    return 1


def get_name():
    return "Cheese Grind"