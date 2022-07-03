# definicion de una funcion para linea 10 y 28
def Saluda():
    print ("Función Saludar", '\n')
#funcion con argumentos
def Saludanombre():
    return "Hola {}, returno de funcion y arreglo {}".format(nombre,vector)
# Primera linea de codigo en Python    
print ("Ingresa tu nombre:")
saludo = ("Hola ")
# Asigna valor string a una variable ingresada por el usuario
nombre = input ()
# funcion de linea 29
Saluda()
# Concatenación
print (saludo + nombre, '\n')
print ("Ingresa valor 1:")
# Asigna valor entero a una variable de tipo string 
Num1 = int (input())
print ("Ingresa un valor a sumar:") 
Num2 = int (input())
# Operadores aritmeticos
resultado = Num1 + Num2
# Casting, cambia un valor entero por una cadena y mostrarla en pantalla
print ("Resultado:", str(resultado),'\n')
# Operadores de comparacion 
if Num1 == Num2:
    print ("Número similar", '\n')
else:
    print ("Números diferentes", '\n')
# Arreglos
print ("Ingresa valor maximo para el arreglo:")
vecmax = int (input())
vector = [vecmax]
print ("Arreglo:", str(vector))
# Declaracionn de funciones, se define y luego se llaman desde cualquier punto.
Saluda()
# Argumentos en funciones con formato, linea 5
print (Saludanombre())
# Sentencias de condicion, While
indice = 0
while indice <= vecmax:
    print ("while", indice)
    indice += 1
print ("Impresiones", indice)
# Ciclo FOR para recorrer una cadena de caracteres
for recorrer in nombre:
    print ("Recorrer cadena", recorrer)
# Ciclo FOR para recorrer un arreglo
for rec in vector:
    print ('\n', rec, vector)
#
my_string = "Aprendiendo lenguaje python "
ult = "que pasa"
result = "{a} de {b}".format (b=ult, a=my_string,)
print (result)
