import keyboard
import mouse
import cv2
import mss
import threading
import time
import numpy as np 

BUY_XY = (1176, 291)
CRUNCH_XY = (955, 435)
CONFIRM_XY = (954, 400)

def main_loop():
       click_listener_thread = threading.Thread(target=keyboard.wait, args=('enter',))
       print('press enter to stop crunching')
       click_listener_thread.start()
       print('Grabbing screen in 5')
       time.sleep(5) 
       while click_listener_thread.is_alive():
              if ready_to_buy():
                     buy_and_crunch_macro()
                     time.sleep(6)
       return 1

def ready_to_buy():
       keyboard.send('k')
       time.sleep(.5)
       with mss.mss() as sct:

              monitor = {"top": 205, "left": 290, "width": 1200, "height": 640}
       
              screenshot = sct.grab(monitor)
              # cv2.imshow("Image", np.array(screenshot))
              # while True:
              #        if cv2.waitKey(25) & 0xFF == ord('q'):
              #               cv2.destroyAllWindows()
              #               break
              if screenshot.pixel(10, 60) == (151,113,74):
                     return True                    
              return False

def buy_and_crunch_macro():
       mouse.move(*BUY_XY, duration=.2)
       time.sleep(.2)

       mouse.press('left')
       time.sleep(.1)
       mouse.release('left')

       keyboard.send('c')

       mouse.move(*CRUNCH_XY, duration=.2)
       time.sleep(.2)

       mouse.press('left')
       time.sleep(.1)
       mouse.release('left')

 
       mouse.move(*CONFIRM_XY, duration=.2)
       time.sleep(.2)

       mouse.press('left')  
       time.sleep(.2)
       mouse.release('left')


def get_name():
    return "Faster Crunch"
     