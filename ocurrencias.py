"""
Pregunta 4
Tienes un arreglo (llamado myArray) con 10 elementos (enteros en el rango de 1 a 9). Escribe un programa en Python que imprima el numero que tiene mas ocurrencias seguidas en arreglo y también imprimir la cantidad de veces que aparece en la secuencia.

El código que llena el arreglo ya esta escrito, pero puedes editarlo para probar con otros valores. Con el botón de refrescar puedes recuperar el valor original que sera utilizado para evaluar la pregunta como correcta o incorrecta durante la ejecución.

Su programa debe analizar el arreglo de izquierda a derecha para que en caso de que dos números cumplan la condición, el que aparece por primera vez de izquierda a derecha será el que se imprimirá. La salida de los datos para el arreglo en el ejemplo (1,2,2,5,4,6,7,8,8,8) sería la siguiente:
Longest: 3
Number: 8

En el ejemplo, la secuencia mas larga la tiene el numero 8 con una secuencia de tres ochos seguidos. Tenga en cuenta que el código que escriba debe imprimir los resultados exactamente como se muestra con el fin de que la pregunta sea considerada válida.
"""
from collections import Counter

myArray = [1,2,4,5,6,7,7,8,8,8]
print(myArray)

# verifica la ocurrencias de un numero en el array
result = Counter(myArray)

counter = {}
for num in myArray:
    counter[num] = counter.get(num, 0) + 1

print()

valores = [[key, val] for (key, val) in counter.items()]

for v in valores:
    if v[1] == max(result.values()):
        print('Longest:',v[1], '\nNumber:',v[0])