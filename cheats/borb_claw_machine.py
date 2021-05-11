import cv2
import mouse
import keyboard
import time
import mss
import numpy as np

PLAY_BUTTON_XY = (325, 319)
CLAW_Y= 192
CHEESE_HUB_XY = (1187, 605)


def main_loop():
    ''' 
    Start game 
    take screenshot
    find curse
    operate claw
    '''
    monitor = {"top": 205, "left": 290, "width": 1200, "height": 640}
    with mss.mss() as sct:
        print('starting game in 5')
        time.sleep(5)
        start_game_macro()
        img = np.array(sct.grab(monitor))
        print('finding curse')
        x, _ = find_curse(img)
        
        # click_listener_thread = threading.Thread(target=keyboard.wait, args=('enter',))
        # print('press enter to stop BLC Time Travl')
        # click_listener_thread.start()
        # print('Grabbing screen in 5')
        # time.sleep(5) 
        #     while click_listener_thread.is_alive():
        #     time_travel()
        #     time.sleep(5)
        # return 1

        while True:
            if operate_claw(x, sct.grab(monitor)):
                print('claw at x value ' + str(x))
                keyboard.press('space')
                
        



def start_game_macro():
    time.sleep(.1)
    keyboard.press('v')
    time.sleep(.1)
    mouse.move(*CHEESE_HUB_XY, duration=.16)
    time.sleep(.2)
    mouse.wheel(-9)
    click_mouse()
    time.sleep(.1)
    keyboard.press('tab')

    mouse.move(*PLAY_BUTTON_XY, duration=.16)
    time.sleep(.2)
    click_mouse()
    time.sleep(.1)
    click_mouse()


def operate_claw(x, img):
    b,g,r = img[x][CLAW_Y]
    if (r,g,b)== (151,113,74):
        img = cv2.circle(img,(x,CLAW_Y), 8,(255,0,0),2)
        cv2.imshow("Image", img)
        while True:
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        return False
    else:
        return True

def find_curse(img) :
    

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours , _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    x,y = find_squares(contours)
   
    return (x,y)


def find_squares(contours):
    i = 0

    for contour in contours:
        if i == 0:
            i = 1
            continue

        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        M = cv2.moments(contour)
        if M['m00'] != 0:
            x = int(M['m10']/ M['m00'])
            y = int(M['m01']/ M['m00'])

        if len(approx) == 4:
            return x,y


    return 0,0 

def click_mouse():
    mouse.press()
    time.sleep(.1)
    mouse.release()

    
def get_name():
    return "Borb Claw Machine"