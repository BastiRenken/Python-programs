from turtle import *
import time

STOP = 2
START = 300

def strecke(n):
    if n <= STOP:
        fd(n)
    else:
        strecke(n/3)
        left(60)
        strecke(n/3)
        right(120)
        strecke(n/3)
        left(60)
        strecke(n/3)

speed(0)
left(60)
for i in range(3):
    strecke(START)
    right(120)

hideturtle()
time.sleep(30)
