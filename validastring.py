''' 
Valida un caracter, devuelve True o False si es numero, alfabetico,
alfanumerico, mayuscula o minuscula
'''
character = input("Ingresa un caracter a verificar: ")
print (f'Resultados Booleanos sobre el caracter "{character}":')
print("Es alfanumérico:", any(char.isalnum()for char in character))
print("Es alfabético:",any(char.isalpha()for char in character))
print("Es numérico:",any(char.isdigit()for char in character))
print("Es minúscula:",any(char.islower()for char in character))
#Uso de .format devuleve el valor booleano en 1 o 0
print("Es Mayúscula: {:_^5}, True = 1, False = 0" .format(any(char.isupper()for char in character))) # {subrayar}