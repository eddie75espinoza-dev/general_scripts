#Iterator

nums = [1, 2, 3]

i_nums = iter(nums) #iterator

#print(i_nums)
#print(dir(i_nums))
print('Iterador: ')
print(next(i_nums)) # next guarda en memoria la ubicacion
print(next(i_nums)) # del ultimo elemento a recorrer pero al llegar
print(next(i_nums)) # al final crea una exception
#print(next(i_nums)) # En este caso genera la exception (StopItaration)

# Genera algo como esto
'''while True:  # Puede ser un bucle infinito sino se controla el while
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break
'''

print('Other example: ')

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums_class = MyRange(1,5)

for i in nums_class:
    print(i)

#Con un ciclo FOR se puede haer el recorrido automaticamente
print('Ciclo For: ')
for num in nums_class:
    print(num)

# con la funcion NEXT se hace la iteracion manualmente
print('Other class example: ')
nums_class = MyRange(1,4)
print(next(nums_class))
print(next(nums_class))
print(next(nums_class))
#print(next(nums_class)) # StopIteration

print('Other Generator example: ')
# los generadores son bastante utiles y faciles para crear iteradores

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums_gener = my_range(1,4)
print(next(nums_gener))
print(next(nums_gener))
print(next(nums_gener))
#print(next(nums_gener)) # StopIteration

# Los generadores no almacenan el resultado completo en la memoria
# produce los resultados 1 por 1
print('Generador: ')
def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1, 2, 3, 4])

#Objeto, espera a que se le envie la siguiente instuccion
# todavia no ha calculado
print(my_nums) 

#Agregando NEXT ejecuta la funcion
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

# Incluso se puede usar aun el ciclo FOR
print('ciclo FOR con el generador: ')
my_nums = square_numbers([1, 2, 3, 4])
for num in my_nums:
    print(num)

# El generador anterior se puede resumir aun mas con LIST COMPRENHENTIOS
print('Lista de comprension:')
my_nums = [x*x for x in [1, 2, 3, 4]]
print(my_nums)

# Se sustituye los [] al inicio y final por () y se usa igual que un for
print('Generador con Lista de comprension:')
my_nums = (x*x for x in [1, 2, 3, 4])
for num in my_nums:
    print(num)

#Se pueden envolver como una lista y generarlos todos sin el for
print('Generador como Lista')
my_nums = (x*x for x in [1, 2, 3, 4])
print(list(my_nums))
