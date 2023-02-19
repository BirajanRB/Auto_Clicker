import mouse
import keyboard
import time

while True:
    if keyboard.is_pressed('p'):
        mouse.click(button='left')
    time.sleep(0.005)
