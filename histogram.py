"""
Histograma: un histograma es una representación gráfica que nos permite 
ver la distribución de las frecuencias de una muestra.


"""

from collections import Counter

edades = [19, 12, 15, 13, 12, 15, 13, 20, 19, 20, 12, 13, 12, 18, 17, 15, 12, 13, 16, 17, 19, 15]

mapa_edades = {} 

for n, edad in enumerate(edades, min(edades)):
    if n == max(edades)+1:
        break
    if n not in mapa_edades:
            mapa_edades[n] = 0 

print(mapa_edades)
edades_mapeadas = Counter(edades)
     
for valor in sorted(mapa_edades):
	print(f'{valor}: {"*" * edades_mapeadas[valor]}')


#### Otro ejemplo

print("§"*5, end="\n")
myArray = [1,2,1,3,3,1,2,1,5,1,6]

def histogram(lst):
    num1, num2, num3, num4, num5 = 0, 0, 0, 0, 0
    for num in lst:
        if num == 1:
            num1 += 1
        elif num == 2:
            num2 += 1
        elif num == 3:
            num3 += 1
        elif num == 4:
            num4 += 1
        elif num == 5:
            num5 += 1
    print('1:', '*'*num1)
    print('2:', '*'*num2)
    print('3:', '*'*num3)
    print('4:', '*'*num4)
    print('5:', '*'*num5)

histogram(myArray)

    