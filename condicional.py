print('Indica una fruta: mango, pera o mamon')
fruta = input()

if  fruta == 'mango': # si y solo si
    print('La fruta es Mango')
elif fruta == 'mamon':
    print('La fruta es Mamón')
else: # es optativo colocarlo
    pass                          # pass hace que no se ejecute nada
    #print('La fruta es Pera')

"""
mensaje = 'La fruta es Mamón' if fruta == 'mamon' else 'Sin fruta'
print(mensaje)
"""
#
