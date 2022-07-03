# Manejo de listas 
my_list = ["Listas", 20, 10.75, True]
my_list.append('insertar al final') #append inserta al final
my_list.insert(2,'insert en la posicion') #insert (indice y objeto)

# my_list.remove (10.75) # remueve el valor indicado
#print (my_list[3]) # imprime la posicion de la lista 3
my_list.pop() # muestra el valor ultimo agragado a la lista
my_list.pop()

print ("My List: ", my_list)
print ("My List .pop: ",my_list.pop())
print ("My List: ", my_list)
my_numb = [7,3,10,15,20,18,2,5,9] # lista con enteros
print ("List Numb: ", my_numb)

my_numb.sort() # ordena la lista en forma creciente
print("List Number ordered: ",my_numb)
my_numb.sort(reverse = True) #oredena la lista al reves
print ("List Numb reversed: ",my_numb)
# concatenar 2 listas
my_numb_2 = [1,4,6,8,11,12,13,14,16,17,19]
#my_list.extend(my_numb_2) # string y int
my_numb.extend(my_numb_2)
print("List Numb 1 & 2: ", my_numb)
# ordenar
my_numb.sort()
print (my_numb)

# reverse de listas
_list = [1, 2, 3, 4, 5, 6]
print("lista: ",_list)
print("Reversed: ", _list[::-1])