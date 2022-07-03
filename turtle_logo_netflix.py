"""
Logo de Netflix diseñado con la libreria Turtle de Python
"""
import turtle
import time

turtle.title('Netflix logo in Python')
turtle.bgcolor('#141414')

turtle.right(90)
pos = [(-40, 0), (40, 0)]
for x, y in pos:
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor('#E50914')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()

turtle.up()
turtle.goto(-40, 0)
turtle.down()
turtle.left(22)

turtle.begin_fill()
for i in range(2):
    turtle.forward(217)
    turtle.left(68)
    turtle.forward(40)
    turtle.left(112)
turtle.end_fill()

time.sleep(7)