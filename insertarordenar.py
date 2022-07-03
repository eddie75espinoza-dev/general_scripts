#Insertion sort
def insertionSort(list):
    for i in range(1,len(list)):
        currentNumber = list[i]
        for j in range(i-1, -1, -1):
            if list[j]>currentNumber:
                list [j], list[j+1] = list[j+1], list [j]
            else:
                list[j+1] = currentNumber
                break
    return list

if __name__ == '__main__':
    list = [3,4,2,6,7,6,5,7,1,9,7,8]
    print('Lista ordenada:', insertionSort(list))
    print ('Valor mas repetido: ',max(set(list), key = list.count)) #verifica el valor mas repetidoS
