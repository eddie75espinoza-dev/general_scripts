# modificacion de variable local
def valor_global():
    global variable_global
    variable_global = 'Cambiar valor' # valor local

def mostrar_global():
    print (variable_global)

def crear_global():
    global nueva_variable
    nueva_variable = 'Nueva variable'

variable_global = 'Variable global'


mostrar_global()
valor_global()
crear_global()
print(variable_global)
print(nueva_variable)

''' prueba'''
count = 1

def doThis():
    global count
    for i in (1, 2, 3):
        print(count)
        count += 1

doThis()
print(count)