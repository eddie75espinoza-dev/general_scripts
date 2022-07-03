"""
Script en Python de Logo de Windows 
background gradiente
"""
from turtle import *
from turtle import Screen, Turtle

setup(520, 420)

# background gradient
COL = (0.60156, 0, 0.99218)  
TAR = (0.86328, 0.47656, 0.31250)  

screen = Screen()
screen.tracer(False)

WID, HEIG = screen.window_width(), screen.window_height()

delt = [(red - COL[index]) / HEIG for index, red in enumerate(TAR)]

tur = Turtle()
tur.color(COL)

tur.penup()
tur.goto(-WID/2, HEIG/2)
tur.pendown()

direction = 1

for distance, y in enumerate(range(HEIG//2, -HEIG//2, -1)):

    tur.forward(WID * direction)
    tur.color([COL[i] + delta * distance for i, delta in enumerate(delt)])
    tur.sety(y)

    direction *= -1

screen.tracer(True)

# logo de window
speed(1)
#bgcolor('#3b83bd')
penup()
goto(-60, 100)
pendown()
color('cyan')
begin_fill()
goto(180, 118)
goto(180, -118)
# draw windows
goto(-60, -80)
goto(-60, -80)
end_fill()
color('cyan')
goto(50, 108)
# cut 2 equal parts
color(COL)
width(5)
goto(50, -100)
penup()
goto(180, 5)
pendown()
goto(-60, 5)
done()