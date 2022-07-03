# Bubble sort
def bubbleSort(list):
    longest = 0
    number = 0
    for i in range(len(list)): 
        for j in range(len(list) -1, i, -1):
            if list [j]< list [j-1]:
                list [j], list [j-1] = list [j-1], list [j]
            
    return list

# 

if __name__ == '__main__':
    list = [4,2,2,3,3,19,6,5,7,11,1,9,8,10,18,13,2,14,17,16,12,20,15]
    print('Lista ordenada:', bubbleSort(list))

    print('Lista ordenada:', sorted(list)) # metodo sorted()