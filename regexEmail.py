'''
Las expresiones regulares son extremadamente poderosas, pero no son la solución correcta 
para todos los problemas.
^ coincide con el comienzo de una cadena.
$ coincide con el final de una cadena.
\b coincide con el límite de una palabra.
\B
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

mailPattern = re.compile(r'''
    [a-z0-9.-_]         # String inicial - firts group
    +@                  # Chr @
    [a-z-]              # segundo string - second group
    +\.                 # Chr . - separator
    ([a-z]{2,3})        # tercer string - third group - e.g com / edu / net / es 
    +(\.+[a-z]{2,3})?   # Opcional hasta 3 caracteres, e.g ar / ve / es 
''', re.VERBOSE)

str_email = input('Ingrese un correo a validar: ')

result = mailPattern.search(str_email) #.groups()      # devuelve True por el Pattern y una tupla por Groups
print("The email {} is valid".format(str_email) if result else "{} is not Valid".format(str_email))