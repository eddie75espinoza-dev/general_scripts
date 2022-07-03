"""
Letra E diseñada con la libreria Turtle de Python
"""
import turtle
import time

turtle.title('Letra E con Turtle in Python')
turtle.bgcolor('#141414')
turtle.right(0)
turtle.fillcolor('#605F5E') # COLOR GRANITE GRAY
turtle.begin_fill()
pos = [(-50, 0)]
for i in range(2):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
turtle.end_fill()
turtle.right(40)
pos = [(-80, -10), (80, 0)]
for x, y in pos:
    turtle.up()
    turtle.goto(y, x)
    turtle.down()
    turtle.left(20)
    turtle.begin_fill()
    for i in range(2):
        turtle.fillcolor('#E2E2E2') # COLOR PLATINUM
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()
    
turtle.right(-70)
pos = [(-85, 0)]
for x, y in pos:
    turtle.up()
    turtle.goto(y, x)
    turtle.down()
    turtle.left(20)
    turtle.begin_fill()
    for i in range(2):
        turtle.fillcolor('#FB3640') # COLOR RED SALSA
        turtle.forward(207)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()


time.sleep(4)