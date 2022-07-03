def fun (x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print(fun(fun(2)))

print("X-/|\-X"*3)
def fun_line(x):
    return "fun line" if x%2==0 else 2

print("def line: 8", fun_line(8))

def fun1(x):
    global y
    y = x*x
    return y

fun1(2)
print(y)

print('++'*5)
def any():
    print(var + 1, end='')

var = 1
any()
print(var)

def fun2(x,y,z):
    return x+2*y+3*z
print(fun2(0, z=1, y=3))

print("**"*5)
def fun3(inp = 2, out = 3):
    return inp * out
print(fun3(out = 2))

dct = {"one": "two", "three": "one", 'two': "three"}
v = dct['one']
for k in range(len(dct)):
    v = dct[v]
print(v)

print("--"*6)
tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

lst = [1,2]
for v in range(2):
    lst.insert(-1, lst[v])
print(lst)

def func1(a):
    return a
def func2(a):
    return func1(a) * func1(a)
print(func2(2))

print(1//2)

z=0
y=10
x = y<z and z>y or y>z and z<y
print(x)

print('=='*5)
list = [x*x for x in range(5)] # lista de comprension
def fun4(lst):
    del lst[lst[2]]
    return  lst
print(fun4(list))

a = 1
b = 0
a = a^b
b = a^b
a = a^b
print('A^: ', a,b)

print('^'*5)

nums = [1,2,3,4]
vals = nums
print(nums)
del vals[:]
print('lista borrada: ', vals)

x=3
y=2
x = x%y
x = x%y
y = y%x
print(y)

x = "3"
y = "6"
print(x+y)

print('~ separador en una cadena ~')
print("a","b","c",sep="sep")
print("2025","12","25",sep="/")
print("100","200","300",sep=".")

print('~'*10)
x = 1//5+1/5
print(x)

x=2.0
y=4.0
print(y**(1/x))

lst = [i for i in range(-1, -2)]
print(len(lst))

print('# # '*4)
def fun5(x,y):
    if x == y :
        return x
    else:
        return fun5(x, y-1)
print(fun5(0, 3))

dct = {}
dct['key1'] = ('key1value1', 'key1value2')
dct['key2'] = ('key2value1', 'key2value2')
print(dct)
print('~ valores desde key')
for x in dct.keys():
    print(x, end=" ")
    print(dct[x][0], end=" ")
    print(dct[x][1])
print('~ valores desde value')
for y in dct.values():
    print(y, end=" ")
    print(y[0], end=" ")
    print(y[1])

