# -*- coding: utf-8 -*-
from calendar import isleap

# del modulo calendar 'isleap' obtiene años bisiestos
for año in range(1904, 2021):
	if isleap(año):       
		print(año, end=' ')

# Ejemplo 1
print()
def es_bisiesto(año):
    # devuelve TRUE si el año es bisiesto
	return not año % 4 and (año % 100 or not año % 400)

# Ejemplo 2
print()
def is_leap(año):
    if not año % 4:
        if not año % 100:     # divisible entre 4 y 100
            if not año % 400:  # divisible entre 4, 100 y 400
                return "-Es bisiesto"
            else:              # divisible entre 4 y 100 y no entre 400
                return "-No es bisiesto"
        else:                 # divisible  entre 4 y no entre 100
            return "-Es bisiesto"
    else:                    # no divisible entre 4
        return "-No es bisiesto"

año = int(input('Indique un año bisiesto: '))
print('funcion 1: ', es_bisiesto(año))
print('funcion 2:', is_leap(año))
#Ejemplo 3
print('funcion 3: ', end='')
print("~Es bisiesto" if not año % 4 and (año % 100 or not año % 400) else "~No es bisiesto")
