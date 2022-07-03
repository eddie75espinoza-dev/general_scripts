lista = [1,2,3,4,5,6,7,8,9,10]
for valor in lista:
    pass
nuevo_rango = range(0,10,2) # dos valores y ultimo valor es el salto
for valor in nuevo_rango:
    #print (valor)
    pass

indice = 1
for indice, valor in enumerate(lista):
    print (valor, 'indice No. ', indice)
    #indice +=1


print (len(lista))
for valor in range(0,):
    pass # print(valor)
for valor in range (0, len(lista)):
    pass # print (valor)

for valor in 'Eddie': # los strings son iterables, los int no
    pass # print (valor)

# recorrer un diccionario
diccionario = {'a': 10, 'b': 20, 'c': 30}
for llave, valor in diccionario.items():
    print('La llave',llave,'tiene el valor',valor)

def x_pattern(n):
    for i in range(0,n):
        for j in range(0,n):
            if i==j or j==n-1-i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

x_pattern(9)