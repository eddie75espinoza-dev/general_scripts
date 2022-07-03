#Python

#    1
#ordenar listas
miLista = [1, 2, 3, 4, 5, 6, 7] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while
print('Lista original: ')
while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] < miLista[i + 1]: #> ASC, < DESC
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print('Lista ordenada: ', miLista)

#    2
#El ordenamiento burbuja - versión interactiva
miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)

#    3
# Listas - algunos programas simples
miLista = [1, 3, 11, 5, 1, 9, 17, 15, 13]
mayor = miLista[0]

for i in range(1, len(miLista)): # tambien se puede usar = for i in miLista [1:]:
   if miLista [i]> mayor:       #   if i > mayor:
        mayor = miLista[i]      #   mayor = i

print(miLista, ' El mayor valor en la lista: ', mayor)

#    4
# Encontrar un valor en la lista
miLista = [1, 3, 11, 5, 1, 9, 17, 15, 13]
Encontrar = mayor
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print(f"Elemento {mayor} encontrado en el índice {i}")
else:
    print("ausente")

#    5
# 
#Encontrar varios valores en una lista

sorteados = [17, 5, 11, 9, 8, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49, 8, 17]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print('N Coincidencias en las listas: ', aciertos)

#   6
# Arreglos tridimensionales
# [expresión for elemento in lista if condicional]
habitaciones =[[[False for r in range(1)] for f in range(2)] for t in range(3)]
print('*** Arreglo trimidensional ***')
print(habitaciones)
print('Asignando valores')
habitaciones[0][0]=1
habitaciones[0][1]=2
habitaciones[1][0]=3
habitaciones[1][1]=4
habitaciones[2][0]=5
habitaciones[2][1]=6

print(habitaciones)

'''salida
[[[False], [False]], [[False], [False]], [[False], [False]]]
[[1, 2], [3, 4], [5, 6]]
'''

#    7
# List Comprehensions
print('List Comprehensions')
x = 1
y = 1
z = 1
n = 2

print( [[i,j,k] for i in range( x + 1) for j in range( y + 1) for k in range(z+1) if ( ( i + j + k ) != n )  ])

#salida : [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# Staircase 1

n=6
for i in range (n+1,0,-1):
        for j in range (i):
            if i == n:
                print("", end='o')
            else:
                print ("#",end = "")
        print ("\r")
'''
salida
#######
oooooo
#####
####
###
##
#

# Staircase 2
'''


#### Year Leap  (a;o bisiesto)
def isYearLeap(year):
    if year % 400 == 0:
       return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

testData = [1900, 2000, 2016, 1987, 2100,2008,1992, 2015]
testResults = [False, True, True, False, False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
##Salida
'''
1900 ->OK
2000 ->OK
2016 ->OK
1987 ->OK
2100 ->OK
2008 ->OK
1992 ->OK
2015 ->OK
'''
