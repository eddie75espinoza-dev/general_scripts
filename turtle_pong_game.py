import turtle
import random
import time

wait = 0.0005

# Ventana
wn = turtle.Screen()
wn.title('Pong Game')
wn.bgcolor('black')
wn.setup(800, 600)
wn.tracer(0)

# Score
score_right = 0
score_left = 0

# definicion de jugadores
# jugador 1 lado derecho
player_right = turtle.Turtle()
player_right.speed(0)
player_right.shape('square')
player_right.color('white')
player_right.penup() # evita la linea desde el punto central
player_right.goto(-380, 0)
player_right.shapesize(stretch_wid=5, stretch_len=0.5) # tamaño de la barra

# jugador 2 lado izquierdo
player_left = turtle.Turtle()
player_left.speed(0)
player_left.shape('square') # forma de barra
player_left.color('white')
player_left.penup() # evita la linea desde el punto central
player_left.goto(380, 0) # posicion de la barra
player_left.shapesize(stretch_wid=5, stretch_len=0.5) # tamaño de la barra, 

# Pelota
color_list = ['#4DEEEA', 'cyan', '#74EE15', '#F000FF', '#FFE700']
col = random.choice(color_list)
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')  # forma de la bola
ball.color(col)   # esta linea cambia el color de la bola en cada partida y el while hace efecto parpadeante      
ball.penup()     # evita la linea desde el punto central
ball.goto(0, 0)
ball.dx = 3     # movimiento en el eje x
ball.dy = -3    # movimiento en el eje y, signo '+' o '-' cambia la direccion de partida

# Score display
led = turtle.Turtle()
led.speed(0)
led.color('white')
led.goto(0, 260)
led.pen()
led.hideturtle()    # oculta el lapiz de turtle
led.write('Score Left: 0                 Score Right: 0', align='center', font=('arial', 24, 'bold'))


# Linea divisoria
line = turtle.Turtle()
line.color('white')
line.goto(0, 400)
line.goto(0, -400)

# Funciones
def player_right_up():
    # movimiento de la bola en el eje y positivo del jugador a la derecha
    y = player_right.ycor()
    y += 20
    player_right.sety(y)

def player_right_down():
    # movimiento de la bola en el eje y negativo
    y = player_right.ycor()
    y -= 20
    player_right.sety(y)

def player_left_up():
    y = player_left.ycor()
    y += 20
    player_left.sety(y)

def player_left_down():
    y = player_left.ycor()
    y -= 20
    player_left.sety(y)


# Teclado
wn.listen()
wn.onkeypress(player_right_up, 'w')
wn.onkeypress(player_right_down, 's')
wn.onkeypress(player_left_up, 'o')
wn.onkeypress(player_left_down, 'l')

while True:
    wn.update()
    color_list = ['#1CEDAE', '#FF0571', '#C2FF05', '#1EFF05', '#E9FF88']
    col = random.choice(color_list)
    ball.color(col) #Permite cambiar de forma aleatoria el color de la bola y crear un efecto parpadeante

    # movimiento de pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # bordes superior e inferior
    if ball.ycor() > 290:   # borde superior
        ball.dy *= -1       # cambia la direccion de la bola
    if ball.ycor() < -280:  # borde inferior, ((600px/2) - 20px(bola) = 280px)
        ball.dy *= -1

    # bordes laterales
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 # Invierte la direccion de la bola
        score_left += 1 # Aumenta el score
        led.clear() # limpia la pantalla para que quede sobreescrito el marcador
        led.write(f"Score Left: {score_left}                 Score Right: {score_right}", align='center', font=('arial', 24, 'bold'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        led.clear()
        led.write(f"Score Left: {score_left}                 Score Right: {score_right}", align='center', font=('arial', 24, 'bold'))

    if ((ball.xcor() > 370 and ball.xcor() < 380)           # Ancho de la barra del jugador 
            and (ball.ycor() < player_left.ycor() + 52)     # Altura de la barra hacia arriba desde el centro
            and (ball.ycor() > player_left.ycor() - 52)):   # Altura de la barra hacia abajo desde el centro
        ball.dx *= -1

    if ((ball.xcor() < -370 and ball.xcor() > -380) \
            and (ball.ycor() < player_right.ycor() + 52) \
            and (ball.ycor() > player_right.ycor() - 52)):
        ball.dx *= -1

    time.sleep(max(0, wait))        # Ralentiza la velocidad de la bola
    wait -= 0.0000001