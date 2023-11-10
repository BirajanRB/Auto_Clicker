import mouse
import keyboard
import time

toggle = False

while True:
    if keyboard.is_pressed('p'):
        mouse.click(button='left')
    
    if keyboard.is_pressed('i'):
        toggle = not(toggle)
    
    if keyboard.is_pressed('o'):
        toggle = False

    if toggle:
        mouse.click(button='left')
        
    time.sleep(0.003)
