# verifica un palindromo
# la variable global puede ser accedida desde la funcion
def palindromo():
    #frase = frase.replace(' ','') # // Variable local, solo en la funcion
    nuevo_valor = frase.replace(" ", '')
    return nuevo_valor == nuevo_valor[::-1]
    #return frase == frase [::-1]
    
#frase = 'anita lava la tina' # Variables locales
frase = input('Frase: ')
resultado = palindromo ()
print (resultado)