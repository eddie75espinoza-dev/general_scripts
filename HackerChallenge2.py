a = int(input())
b = int(input())

def add (a,b):
    addNum = a + b
    print(addNum)
    return addNum

def substract (a,b):
    restNum = a-b
    print(restNum)
    return restNum

def multi(a,b):
    multNum = a * b
    print(multNum)
    return multNum
if (a >= 1 and a <= 10000000000) and (b >= 1 and b <= 10000000000):
    add(a,b)
    substract(a,b)
    multi(a,b)