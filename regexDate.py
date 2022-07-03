'''
Las expresiones regulares son extremadamente poderosas, pero no son la solución correcta 
para todos los problemas.
^ coincide con el comienzo de una cadena.
$ coincide con el final de una cadena.
\b coincide con el límite de una palabra.
\d coincide con cualquier dígito numérico.
\D coincide con cualquier carácter no numérico.
x?coincide con un x carácter opcional (en otras palabras, coincide con un x cero o una vez).
x*coincide con xcero o más veces.
x+coincide xuna o más veces.
x{n,m}coincide con un x personaje al menos n veces, pero no más de m veces.
(a|b|c)coincide exactamente con uno de a, b o c.
(x)en general es un grupo recordado . Puede obtener el valor de lo que coincide utilizando 
el groups() método del objeto devuelto por re.search.

'''
import re

datePattern = re.compile(r''' 
    ^(\d{4})                    # Grupo de 4 digitos para el a;o
    \D                          # Separator optional
    (\d|0[1-9]|1[0-2]|\w{3,10}) # 1 o 2 digitos para el mes, o hasta 10 caracteres para el mes, permmite 3 caracteres para abbr mes
    \W                          # Separador Opcional
    (\d|0[1-9]|[12]\d|3[0-1])   # finaliza con cualquier digito del 1 al 31
    $                           # fin de string
    ''', re.VERBOSE)

dateOfBirth = input('Ingrese fecha de nacimiento a validar: ')

result1 = re.search(datePattern, dateOfBirth)  # devuelve True por el Pattern y una tupla por Groups
result2 = datePattern.search(dateOfBirth) #.groups()      # devuelve True por el Pattern y una tupla por Groups
print('Is valid' if result1 else 'No Valid')
print('Date valid' if result2 else 'Date No Valid')
try:
    print(result1.groups())
    print(result2.groups())
except AttributeError:
    print('Error in date')
