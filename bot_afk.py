import pyautogui as pg
import random
import time

while True:
    x = random.randint(500,700)
    y = random.randint(100,500)
    pg.moveTo(x,y, 0.5)
    time.sleep(random.random()*2)
    