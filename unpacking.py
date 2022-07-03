## desempacado de tuplas, listas, diccionarios

tup = (1, 2, 3, 4)
a, b, c, d = tup
print("Tupla: ", tup)
print(a, b, c, d)

lst = [a, b, c, d]
a, b, c, d = lst
print("Lista: ", lst)
print(a, b, c, d)

dic = {"a": 1, "b": 2, "c": 3}
print("Diccionario: ", dic)
a, b, c = dic.items()
print(a, b, c)

a, b, c = dic.keys()
print(a, b, c)

a, b, c = dic.values()
print(a, b, c)

a, b, c = dic
print(a, b, c)

string = "Eddie"
print("String: ", string)
a, b, c, d, e = string
print(a, b, c, d, e)

coords = ["34° 19' 2.7120\" S", "58° 59' 17.0520\" W"]
print("Coords: ", coords)
x, y = coords
print(x, y)

