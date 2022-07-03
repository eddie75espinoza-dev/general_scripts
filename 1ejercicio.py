"""
Encuentre los errores en el script

Posible resepuesta:
1.- Creará una lista (birthdays) con el segundo argumento posicional (age) 
pasado a la función, es decir, en el ciclo "for" incluirá los números del 
1 al 27 y del 1 al 45.
2.- Error en la linea 5: No es descifrable lo que se pretende hacer con la lista, 
no es un diccionario.

"""

def birthday_function(name, age, birthdays=[]):
    birthdays_history = {}
    for birthday in range(1, age + 1):
        birthdays.append(birthday)
        #birthdays_history[name.split()] = birthdays
        
    print(f"{name}: {birthdays} {name.split()}")

birthday_function("juan", 27)
birthday_function("pedro", 45)
