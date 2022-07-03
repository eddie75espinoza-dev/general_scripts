"""
DEV: Eddie Espinoza

Ejercicio 1:

Existe un tablero (tipo de ajedrez) y una ficha que se puede mover de a un paso a cualquiera de los 8 casilleros adyacentes (izquierda, arriba, diagonal, etc.) A cada casillero del tablero le corresponde una coordenada, en pares ordenados de números, donde(0, 0) es el primero. 

Tenés que programar la solución que, dada una lista de coordenadas, indique el número mínimo de pasos que debe realizar la ficha para visitar cada coordenada, en el orden dado. La ficha comienza en la primera coordenada de la lista.

Un input de ejemplo podría ser:

[ (0, 0), (1, 2), (1, 3) ]

Y la solución en este caso es 3.

| |X|
+-+-+-+-
| |X| | 
+-+-+-+-
| | | | 
+-+-+-+-+
|I| | | |
+-+-+-+-+-+-+

Una ilustración de este caso: I es donde arranca, va en diagonal hacia arriba a la derecha, luego dos veces hacia arriba. Con estos 3 pasos visita las 3 coordenadas.

"""
# Definicion del tablero
table = [ (0, 0), (1, 2), (1, 3),(1,4) ]
arr = [] # array para las filas

# coordenada de busqueda, la posición 0 es fija y las posiciones 1 y 2 se pueden seleccionar
def find_coord(n=1) -> list:
    """
    transforma la tupla a lista para compararlo en la funcion steps
    """
    return list(table[n]) 

# ciclo para rellenar las coordenadas segun el valor maximo de la tabla inicial
for i in range(max(max(table))+1):
    sub_arr = [] # arrays internos de cada fila
    for j in range(max(max(table))+1):
        val_in = [i, j]
        sub_arr.append(val_in)
    arr.append(sub_arr)

def steps(arr: list, n:int) -> int:
    """
    determina la cantidad de pasos para obtener la posicion indicada
    devuelve un valor entero segun la posicion
    """
    count = 0
    for i in range(len(arr)):                     
        for j in range(len(arr[i])):
            if arr[i][j]== n:
                count += j
                break
    yield count 

print(next(steps(arr, find_coord(1))))  # dos pasos a la posicion (1,2)
print(next(steps(arr, find_coord(2))))  # tres pasos a la posicion (1, 3)
print(next(steps(arr, find_coord(3))))  # cuatro pasos a la posicion (1,4)

