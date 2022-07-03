'''
Given an array of integers, calculate the ratios of its elements that are positive, negative,
and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
'''

def plusMinus(arr):
    zero = 0
    posi = 0
    nega = 0
    for num in arr:
        if num == 0:
            zero += 1
        elif num > 0:
            posi += 1
        else:
            nega += 1

    posi /= n
    posi = round(posi,6)
    posv = (str(posi)).ljust(8,'0')
    print('% Positivos: ', posv)
    nega /= n
    nega = round(nega,6)
    negv = (str(nega)).ljust(8, '0')
    print('% Negativos: ', negv)
    zero /= n
    zero = round(zero, 6)
    zerv = (str(zero)).ljust(8, '0')
    print('% Cero: ', zerv)


n = int(input('Ingrese la cantidad de numeros para la matriz: '))

arr = list(map(int, input('Ingrese numeros matriz separados por espacios: ').rstrip().split()))

plusMinus(arr)