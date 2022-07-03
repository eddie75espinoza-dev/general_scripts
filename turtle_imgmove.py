import turtle

screen = turtle.Screen()
image = "C:\\Users\\Usuario\\Downloads\\ship1.gif"
# this assures that the size of the screen will always be 400x400 ...
screen.setup(900, 600)

# ... which is the same size as our image
# now set the background to our space image
screen.bgpic("C:\\Users\\Usuario\\Downloads\\space.png")

# Or, set the shape of a turtle
screen.addshape(image)
turtle.shape(image)

move_speed = 30
turn_speed = 30

# these defs control the movement of our "turtle"
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

turtle.penup()
turtle.speed(10)
turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

screen.mainloop()