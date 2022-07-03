# .format
my_string = "Aprendiendo Lenguaje Python "
ult = "cOn Cadenas De Caracteres"
result = "{} {}".format (my_string, ult)
# cambio de cadena a minusculas
result = result.lower()
# cambio de cadenas a mayusculas
#result = result.upper()
# formato de titulo
result = result.title ()
print (result)
""" metodos de busqueda """
pos = result.find("Python") # hubica la posicion 
print (pos) # 
count = result.count('a') # veces que aparece un caracter
print (count)
# metodo de sustitucion
new_string = result.replace('e','E')
#
new_string = result.split(' ')
print(new_string)

# Color en consola
print("\033[96mColor light green")
print("\033[91mColor red")
print("\033[92mColor Green")