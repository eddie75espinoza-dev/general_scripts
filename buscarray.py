# -*- coding: utf-8 -*-
#Decoración: Nombre del Algoritmo
print("--------------------------------")
print("BUSCAR ELEMENTO DENTRO DEL ARRAY")
print("--------------------------------")
#Inicializar
valor = []
#Entradas
print ("Ingrese número de elementos del arreglo")
m = int( input())
print ("Ingrese los elementos del arreglo")
for i in range(m) :
    elemento = int( input("Ingrese Elemento: "))
    valor.append(elemento)
#Búsqueda del valor dentro del arreglo
print ("Ingrese el valor buscado: ")
bus = int( input())
print ("La posición del valor buscado será:")
for i in range(m) :
    if valor[i] == bus :
        r = i
        print ("La posición del elemento es ", r + 1)
        break
