# -*- coding: utf-8 -*-

# manejo de diccionarios dentreo de {}
diccionario = {'a': 'primero', 'b': 2, 'c': True, 'd': 4 }
# incluir
diccionario['e'] = 'quinto'
print(diccionario)
# actualiza un valor existente
diccionario['c'] = 3
print(diccionario)
#obtener un valor del diccionario
#opcion 1, complicada
# valor = dicionario ['z']
#opcion 2, metodo get
valor = diccionario.get('z')
print ('Indice buscado:',valor)
# Objeto iterable
llaves = tuple(diccionario.keys()) # indice, clave o llave
print ('Indice:',llaves)
valores = tuple(diccionario.values()) # valores del diccionario
print('Valores:',valores)
# incluir otro diccionario
diccionario_dos = {'f': 'seis', 'g': 8, 'h': True}
#diccionario['f'] = diccionario_dos['f'] # no es la forma mas comoda
#diccionario['g'] = diccionario_dos['g']
diccionario.update(diccionario_dos)
print(diccionario)

print('=='*20)

dct = {}
dct['key1'] = ('key1value1', 'key1value2')
dct['key2'] = ('key2value1', 'key2value2')
print(dct)
print('~ valores desde key')
for x in dct.keys():
    print(x, end=" ")
    print(dct[x][0], end=" ")
    print(dct[x][1])
print('~ valores desde value')
for y in dct.values():
    print(y, end=" ")
    print(y[0], end=" ")
    print(y[1])

print(dct.get('key1'))

powerstats = {'intelligence': 75, 'strength': 7, 'speed': 21, 'durability': 10, 'power': 100, 'combat': 50}

valor = [[key, val] for (key, val) in powerstats.items()]
print(valor[0][0],':',valor[0][1])