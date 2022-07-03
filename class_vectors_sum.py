# date 22/02/2022
# Suma de Vectores a traves de uso de clases
# se puede cambiar la operación a cualquiera otra

class Vector:

    def __init__(self, x: int, y:int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        # Add vector
        return (self.x + other.x, self.y + other.y)

    def __subt__(self, other):
        # Subtract vector
        return (self.x / other.x, self.y / other.y)

    def __mul__(self, other):
        # Mult vector
        return (self.x * other.x, self.y * other.y)

    def __repr__(self) -> str:
        (self.x, self.y)

    
v1 = Vector(12, 18)
v2 = Vector(2, 4)
v5 = Vector(7,3)

v3 = v1 + v2
v4 = v1 * v2
#v7 = v5 - v2

print(v1.x, v1.y)
print(v2.x, v2.y)
print('sum:  ', v3)
print('mult: ', v4)
#print('subt:', v7)