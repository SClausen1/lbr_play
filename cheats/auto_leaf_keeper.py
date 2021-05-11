import mouse 
import threading 
import keyboard
import pickle


    
    

def mouse_mover(record):
    while True:
        mouse.play(record)

def main_loop():
    with open("recordings/auto_leaf_keeper.pkl", 'rb') as input:
        record = pickle.load(input)
    print('press enter to stop auto leaf keaper')
    click_listener_thread = threading.Thread(target=keyboard.wait, args=('enter',))

    click_listener_thread.start()

    while click_listener_thread.is_alive():
        mouse.play(record, speed_factor=10)

    return 1

def get_name():
    return "Auto Leaf Keeper"