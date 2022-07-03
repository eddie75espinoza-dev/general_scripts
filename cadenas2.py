# Reversing a string
string = "sulPremmargorP"
print ("reverse is", string[::-1]) # muestra en reversa una cadena string, si se amplia salta varios espacios
# Swap two numbers with one line
first, second = 1,2 
print(first, second)
first, second = second, first
print(first, second)
# Check the memory usage of an object
import sys
num = 2
print(sys.getsizeof(num))
# Print string N times
s,n = "ProgrammerPlus", 4 # string a repetir y numero de veces a repetir
print(s*n)
#Create a simple string from all the elements in list
list = ["Python","string","here"]
print(" - ".join(list))
#Store all three values of the list in 3 new variables
list = [1,2,3,4]
w,x,y,z = list
print(w,x,y,z)
# Imprimir una cadena de dos lineas o con variable
print("Mensaje de 2 "
"lineas")
msg = "Otro mensaje " \
    "con 2 lineas con \\" # si se omite "\" solo imprime una linea
print(msg)

msg1 = '''Otro mensaje \
    con 2 lineas con \''' ''' # si se coloca "\" lo imprime en una linea
print(msg1)

#===================================
string = "Esto es solo una oración". 
resultado = string.swapcase ()
print (resultado) # ESTA ES SOLO UNA SENTENCIA.