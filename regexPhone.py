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

Forma de agrupar el telefono:
[Código internacional (00) o (+1)] + [Código del país] + [Código regional] + [Número telefónico]
'''
import re

phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d*?)       # country code is 3 digits (e.g. '001')
    \D*         # optional separator
    (\d{0,3})   # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{0,4})   # trunk is 4 digits (e.g. '0555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)


my_phone = input('Ingrese teléfono: ')
result = phonePattern.search(my_phone).groups()
result1 = phonePattern.search('work 1-(800) 555.1212 #1234').groups()

result2 = phonePattern.search('1-800-555-1212')

print(result)
print(result1)
print(result2)