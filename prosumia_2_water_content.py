"""
DEV: Eddie Espinoza

Ejercicio 2:

Dada una tira de números que representa las alturas del perfil de un terreno, calcular el agua que queda atrapada entre las cimas en caso de lluvia.

Por ejemplo, el arreglo [ 5, 3, 1, 1, 3, 1 ] se corresponde con las alturas del perfil:

#
#
# # x x #
# # x x #
# # # # # #
-----------
5 3 1 1 3 1
Donde x indica agua acumulada. La primera columna es altura 5, segunda 3, etc. Notar que no cabe más agua pues se escurriría por el margen derecho. En este caso la solución es 4.

"""

def max_value(ground):
    return max(ground)

def refill(lst):
    lst_pick = []
    for i in lst:
        for j in range(i):
            sub_arr = [i for k in range(j+1)]
            for s in sub_arr:
                if len(sub_arr) != max_value(lst):
                    sub_arr.append('x')
        lst_pick.append(sub_arr)

    return lst_pick

def inver_lst(arr):
    result_partial = []  
    result = []     
    for i in range(len(arr)): 
        for x in arr:
            sub_result = x[i-1]
            #print(x[i], end =' ')
            result_partial.append(sub_result)
        result.append(result_partial)    
        #print()
        
    return result

def separate_arr(arr): 
    new_list = []
    arr = arr[0]
    for i in range(0, len(arr), 6):
        new_list.append(arr[i:i+6])
    
    return new_list

def validate(arr):
    pass
    
if __name__ == "__main__":
    ground = [5, 3, 1, 1, 3, 1 ]
    
    arr = refill(ground)
    result_lst = inver_lst(arr)
    
    print(separate_arr(result_lst))
    