# suma diagonales en una matriz
def diagonalDifference(arr):
    sum_first_diagonal = sum(arr[i][i] for i in range(n))
    sum_second_diagonal = sum(arr[i][n-i-1] for i in range(n))
    print(sum_first_diagonal)
    print(sum_second_diagonal)
    result = abs(sum_first_diagonal-sum_second_diagonal)
    return result
n = int(input("Ingresa un numero para la matriz de array: ").strip())

#arr = [[5,2,9],[4,5,6],[9,8,5]]
arr=[]
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(result)