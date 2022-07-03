matriz = ['a', 'b', 'c','d', 'd','c','b','a']
#matriz = ['a', 'b', 'c','d', 'c','c','b','a']

def symmetric(matriz):
    return matriz == matriz[::-1]

if symmetric(matriz):
    print('Symmetric')
else:
    print('Asymmetric')