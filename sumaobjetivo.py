# -*- coding: utf-8 -*-
"""  POR COMPLETAR
Dado una lista de numeros enteros y un numero objetivo, hayar los indices que suman el numero objetivo usando solo 1 ciclo for.

input:
lista de numeros = 1,2,3,4,5,6,7,8,9
numero objetivo = 5

output:
[ 1, 2 ]

Hints:
indice 1 = numero 2
indice 2 = numero 3
suma(valor de indice 1 + valor de indice 2) = numero objetivo(5)

"""

""" def twoSum(arr, target):
    diff = {}
    for i in range(len(arr)):
        n = arr[i]
        validate = target - n
        print(validate)
        if validate == 0:
            return [i,]
        if validate - target:
            diff[i] = {
            'i': i,
            'value': target - n
            }
            k, l, m = diff.keys()
        print(k, l, m)
    return [] """

def twoSum(arr, target) -> list:
    print(arr, target)
    lst_num = {}
    for index, num in enumerate(arr):
        n = arr[index] + arr[index + 1]
        if n == target:
            print(n)
            return [index, index + 1]
        lst_num = {
            'index' : index,
            'value' : num
        }
        
    return []


if __name__ == "__main__":
    number_list = [6,3,4,9,1]
    print(twoSum(number_list, 10))
