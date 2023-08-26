from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import threading
from time import sleep

on_off_button = KeyCode(char='-')
clicking = False
mouse = Controller()

def auto_clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        sleep(0.0001)

def input_checks(button):
    if button == on_off_button:
        global clicking
        clicking = not clicking

thread = threading.Thread(target=auto_clicker)
thread.start()

with Listener(on_press=input_checks) as listener:
    listener.join()