#ciclo while
contador = 0
Variable = True #booleano
while Variable :           # contador o Variable
    print(contador)
    contador += 1
    if contador == 5:
        print('mitad')  
    if contador == 6:
        continue
    if contador == 7:
        #break                  # termina de forma abrupta while
        Variable = False
else:
    print('el ciclo ha terminado')

