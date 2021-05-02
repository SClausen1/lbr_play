import mouse 
import threading 

def mouse_script():
    print("Left click to start and stop recording your mouse")

    mouse.wait('left')
    
    print("recording...")

    record = mouse.record(button='left')

    print("recording finished")

    print('Left click to reclaim your mouse')

    main_loop(record)
    
    print('Goodbye')

def mouse_mover(record):
    while True:
        mouse.play(record)

def moouse_main_loop(record):
    click_listener_thread = threading.Thread(target=mouse.wait, args=('left','double'))

    click_listener_thread.start()

    while click_listener_thread.is_alive():
        mouse.play(record)

