# future comprehension
# Lista de 100 elementos
"""
lista = []
for valor in range (0,101):
    lista.append(valor)
print (lista)
"""
# List Comprenhension
lista = [valor for valor in range (0,101) if valor % 2 == 0]
# 1- valor a agregar
# 2- ciclo, for     
# 3- no mas de ahí
tupla = tuple((valor for valor in range (0,101)if valor % 2 != 0))

dicc = {indice:valor for indice, valor in enumerate(lista) if indice < 20}
print(lista)
print (tupla)
print (dicc)
'''
Utilizando expresiones lambda en Python y/o  list comprehension, 
crear un codigo que dado una lista de enteros (tu entrada) pasada por parametro, 
devuelva una lista en la cual cada elemento, sea el doble de cada elemento 
de la lista de entrada.

Ejemplo:

Entrada : [2,4,6,8]
Salida: [4,8,12,16]
'''
print('Lista doble')
listNum = [2,4,6,8]
listNumDouble = [num * 2 for num in listNum] 

print(listNumDouble)