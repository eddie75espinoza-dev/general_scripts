n = 5
for line in range (1,n+1):
    for star in range (line):
        print('#', end = "")
    print ("\r")

print('---')
n= 5
for i in range (1,n+1):
        print(str('o'* i).rjust(n))

print('---')
n= 5
for i in range (1,n+1):
        print(str('o'* i).ljust(n))
print('---')
n= 6
for i in range (1,n+1):
        print(str('o'*i).center(8))
