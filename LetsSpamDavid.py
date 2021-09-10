#Fully wrote by MD5Hashm on github

import random
import time
from pynput.keyboard import Key, Controller
from pynput.keyboard import Key, Listener

keyboard = Controller()

message = input('Please input the message you would like to spam: ')

hi = 1

time.sleep(4)

while hi == 1:
    keyboard.type(message)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.22)
