'''

'''
# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    xyz=[]
    xyz.append(x)
    xyz.append(y)
    xyz.append(z)
    xyz.sort()
    a = abs(x - z)
    b = abs(z - y)

    if a == b:
        print('C: ',a,b)
        return 'Mouse C'
    elif b > a:
        print('A: ', a, b)
        return 'Cat A'
    else:
        print('B: ', a, b)
        return 'Cat B'


if __name__ == '__main__':

    q = int(input('cantidad iteraciones: '))

    for q_itr in range(q):
        xyz = input('3 valores separados: ').split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
    print(result, '\n')