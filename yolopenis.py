import random
import time
import pynput
from pynput.keyboard import Key, Controller
from pynput.keyboard import Key, Listener
from pymouse import PyMouse

m = PyMouse()
keyboard = Controller()


time.sleep(4)

pos = m.position()

print(pos)

pos1 = input('pos1 ')
pos2 = input('pos2 ')

pos1int = int(pos1)
pos2int = int(pos2)

hi = 1

time.sleep(4)

while hi == 1:
    message = random.randint(100, 100000)
    messagestr = str(message)
    keyboard.type(messagestr)
    time.sleep(1)
    m.click(pos1int, pos2int)
    time.sleep(2.5)
    keyboard.press(Key.ctrl)
    keyboard.press('r')
    keyboard.release('r')
    keyboard.release(Key.ctrl)
    time.sleep(6)