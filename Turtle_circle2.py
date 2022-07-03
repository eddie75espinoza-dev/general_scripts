import turtle

t = turtle.Turtle()
ws = turtle.Screen()

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)

while(True):
    for i in range(6):
        for colors in ['red', 'blue', 'white', 'green', 'yellow', 'magenta']:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)

    ws.exitonclick()
turtle.hideturtle()
turtle.mainloop()
