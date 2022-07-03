#Program to remove puntuations from a string
#define puntuations
puntuations = '+-''°!"#$%&/()=?¿¡*]¨[:;_´{<>^`~\¬}.,' #Colocar los caracteres a eliminar, acá estan los comunes 
#faltarian los no frecuentes, es decir con ALT+ como @
#my_str = "Hello/*-!!!, my$%&/() name is ¨+, {eddie}."
#o take input from the user
my_str = input ("Ingresa un texto para eliminar caracteres especiales: ") 
#remove puntuations from the string
no_pun = ""
for char in my_str:
    if char not in puntuations:
        no_pun = no_pun + char
#
print(no_pun)