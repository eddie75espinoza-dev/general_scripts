# -*- coding: utf-8 -*-
"""
Date 04/2/2022
Dev: Eddie75Espinoza

Dado un numero de serie de un billete de euro validar que este es valido.

hints:
- convertir letra en su correspondiente posicion del alfabeto
- sumar cada numero de la serie para obtener la decena
- separar la decena y sumar para obtener el resultado, siempre el valor 8
- un resultado distinto debe indicar que la serie es INCORRECTA

input:
serie : X15783971789

output

result : 8

ejemplo:
x = 24
24 + 1 + 5 + 7 + 8 + 3 + 9 + 7 + 1 + 7 + 8 + 9 = 89
89 = 8 + 9 = 17
17 = 1 + 7 = 8 -> Resultado correcto

"""
# library
import re
from xxlimited import Str

print('-'*40)
print('Valida Serie de Billete de Euro'.center(40))
print('-'*40)

def sum_lst(lst: list) -> int:
    '''
    Recibe una lista de string de numeros y los suma a manera de reduce().
    '''
    res_num = 0
    for i in lst:
        res_num += int(i)
    return res_num

def check_serie_euro(serie: str) -> int:
    '''
    Dada una serie de un billete valida si es Verdadero o Falso. ~
    serie -> formato de 1 letra y 11 numeros. ~
    return -> 8 si es Verdadero, otro numero es Falso.
    '''
    lat_alpha = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
    char_pattern = re.compile(r"(^\D?)(\d{0,11})",re.VERBOSE)
    # obteniendo los grupos de la serie
    result_group = char_pattern.search(serie).groups()
    # obteniendo los valores de los grupos
    char_group = result_group[0].lower()
    number_group = list(result_group[1])

    for i, char in enumerate(lat_alpha):
        if char_group == char:
            r = i
            pos_alpha = r + 1
            break
    
    sum_num = sum_lst(number_group)
        
    res = sum_num + pos_alpha
    
    res_num = sum_lst(list(str(res)))
    
    final_res = sum_lst(list(str(res_num)))
    
    return final_res


if __name__ == '__main__':
    serie = 'X15783971789'
    print('Serie de billete: ', serie)
    result = check_serie_euro(serie)
    print('La serie es CORRECTA' if result == 8 else 'La serie es INCORRECTA' )