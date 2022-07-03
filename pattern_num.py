"""
  1
 212
32123
 212
  1

"""
n = 5
space = n // 2
num = 1


for i in range(1, n+1):
    for j in range(1, space+1):
        print(" ", end="")
    count = num // 2 + 1
    for k in range(1, num+1):
        print(count, end="")
        if (k <= num // 2):
            count -= 1
        else:
            count += 1
    print()
    if (i <= n //2):
        space -= 1
        num += 2
    else:
        space += 1
        num -=2
            