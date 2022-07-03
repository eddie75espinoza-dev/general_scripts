lista = [[5, 3, 'x', 'x', 3, 'x'],[5, '3', 'x', 'x', '3']]
lista_str = '53xx3x'
char_found = 'x'
def validate(lista):
    stack = []
    counter = 0
    conver = lista.split('x')
    for i in lista:
        if str(i).isnumeric():
            print(i)
        if str(i)=='x':
            counter+=1
    return counter, conver

print(validate(lista_str))

lst = []
for pos,char in enumerate(lista_str):
    if(char == char_found):
        lst.append(pos)
print(lst)

count = 0
for i in lst:
    if i == len(lista[0]):
        pass