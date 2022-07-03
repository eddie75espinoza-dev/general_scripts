"""
Libreria Turtle
Acepta solo imagenes GIF y PNG
"""
import turtle
import time

tr = turtle.Turtle()
wn = turtle.Screen()
wn.title('Background image in Turtle')

wn.setup(720, 400) # dimensiona el screen
wn.bgcolor('#f6511d') # f6511d, redorange / ffb400 honey yellow / 7fb800 apple green / 00a6ed carolina blue / 
#wn.setworldcoordinates(-100, -520, 100, 200) # Posiciona la imagen en el screen
#wn.bgpic("C:\\Users\\Usuario\\Downloads\\netflix.gif")
wn.bgpic("C:\\Users\\Usuario\\Downloads\\mclaren1.png")
wn.update() 

time.sleep(2)
wn.bgcolor('#ffb400')
wn.bgpic("C:\\Users\\Usuario\\Downloads\\mclaren2.png")
wn.update() 

time.sleep(2)
wn.bgcolor('#00a6ed')
wn.bgpic("C:\\Users\\Usuario\\Downloads\\mclaren1.png")
#tr.write('F1in Python')
wn.exitonclick() # Cierra la aplicacion con el evento click
wn.mainloop()