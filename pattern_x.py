"""
Pregunta 1
Escribir un programa en Python que imprima una X construida a base de la letra X y utilizar el carácter de subrayado como espacio. El tamaño de la x se basa en una variable n que indicará el tamaño de la letra para imprimir (en una matriz de n x n). Por ejemplo, para n = 5 se obtiene:

X___X
_X_X_
__X__
_X_X_
X___X

y para n=6 se obtiene:

X____X
_X__X_
__XX__
__XX__
_X__X_
X____X

Si n es igual a cero imprimir "ERROR"

El código para el tamaño de n ya está ahí, puede editarlo para probar con otros valores y puede hacer clic en el botón de actualización junto a él para volver al valor original que se utiliza para validar su código durante la prueba. Tenga en cuenta que el código debe imprimir los resultados exactamente como se muestra con el fin de que la pregunta sea considerada valida durante la prueba (El caracter "X" en mayúscula y el guion bajo "_" para los espacios)
"""
n=5

def pattern_x(size):
    i,j = 0,size - 1
    if size == 0:
        print('ERROR')
    else:
        while j >= 0 and i < size:

            initial_spaces = '_'*min(i,j)
            middle_spaces = '_'*(abs(i - j) - 1)
            final_spaces = '_'*(size - 1 - max(i,j))

            if j == i:
                print (initial_spaces + 'X' + final_spaces)
            else:
                print (initial_spaces + 'X' + middle_spaces + 'X' + final_spaces)

            i += 1
            j -= 1

pattern_x(n)