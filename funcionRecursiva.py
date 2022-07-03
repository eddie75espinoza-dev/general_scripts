#
def factorial_numero(number): # con el () vacio se indica variable number
    # dentro ( ) colocar el argumento
    factorial = 1
    while number > 0:
        factorial = factorial * number
        number -=1
    print ("Desde la función: ", factorial) # imprime desde la funcion
    return factorial  #  con return devuelve valor y sin return es None



# recibir argumentos dentro de ()
resultado = factorial_numero (4)
print ("Con return : ",resultado)
factorial_numero(5)
factorial_numero(6)
