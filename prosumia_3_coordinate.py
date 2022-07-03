"""
DEV: Eddie Espinoza

Ejercicio 3:

Una regla tiene la siguiente forma: "A S B" la cual simboliza que el punto "A" está al sur(S) del punto "B". Crear un algoritmo que decida si un conjunto de reglas son consistentes. Por ejemplo:
A S B
C S A
C NO A
Es inválido

B NE A
D SE B
E SE A  
B NO E # aqui el punto B NE E 
Es válido

Las reglas pueden contener 8 direcciones cardinales: norte (N), este (E), sur (S), oeste (O), noreste (NE), sureste (SE), suroeste (SO) y noroeste (NO).

"""
import numpy as np


coordinates_dic = {
    "NO" : 0,
    "N" :  1,
    "NE" : 2,
    "O" :  3,
    "XY" : 4,
    "E" :  5,
    "SO" : 6,
    "S" :  7,
    "SE" : 8
}

class Point:
    def __init__(self, x, y, coord) -> None:
        self.x = x
        self.y = y
        self.coord = coord

    def assign_value(self):
        rows, column = 3, 3
        ma = []
        elem = 0
        for i in range(rows):
            row = []
            for j in range(column):
                row.append(elem)
                if elem == coordinates_dic[self.coord]:
                    row.pop()
                    row.append(self.y)
                if elem == 4:
                    row.pop()
                    row.append(self.x)
                    
                
                elem += 1
            ma.append(row)
        return ma

    def __repr__(self) -> str:
        (self.x, self.y)


def assign_array_values(arg):
    position, fixed, coord = [*arg]
    fixed = coordinates_dic["XY"]
    position = coordinates_dic[coord]
    if coord in coordinates_dic:
        coord_num = coordinates_dic[coord]
    return [position, fixed, coord]


if __name__ == '__main__':
    xy = list(map(str, input("matriz a separada por espacios (3): ").upper().rstrip().split()))
    qz = list(map(str, input("matriz b separada por espacios (3): ").upper().rstrip().split()))
    
    # Usando Clases
    point_a = Point(xy[2], xy[0], xy[1])
    point_b = Point(qz[2], qz[0], qz[1])
    
    repr_a = point_a.assign_value()
    repr_b = point_b.assign_value()

    print(repr_a)
    print(repr_b)

    if repr_a == repr_b:
        print("Es Válido")
    else:
        print("No es Válido")

    # Usando Listas
    lst_1 = [xy[2], xy[0], xy[1]]
    lst_2 = [qz[2], qz[0], qz[1]]
    position, fixed, coord = lst_1
        
    lst_xy = assign_array_values(lst_1)
    lst_qz = assign_array_values(lst_2)
    print(lst_xy)
    print(lst_qz)
    
    if lst_xy == lst_qz:
        print("Es Válido")
    else:
        print("No es Válido")

    # Con Numpy
    P = np.array(lst_1)
    T = np.array(lst_2)

    C = np.intersect1d(P, T) # Punto de interseccion

    if not (P == T).all():
        print(C)
    else:
        print("No es válido")