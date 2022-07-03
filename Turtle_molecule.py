from turtle import *
import time
import random

speed(20)
colors = ['cyan', 'dark cyan', 'darkturquoise', 'turquoise', 'powderblue']
bgcolor('black')
pensize(0.5)
b = 200
forward(260)
while b > 0:
    color(random.choice(colors))
    left(b)
    forward(b*3)
    b = b - 1

time.sleep(6)