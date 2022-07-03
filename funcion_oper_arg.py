def calculo (*arg):
    return {
         'sum': lambda: a+b,
         'res': lambda: a-b,
         'mult': lambda: a*b,
         'div': lambda: a/b
    }.get(op,lambda: None)()


op, x, y = input('~Sum~Res~Mult~Div~ valor1 valor2: ').split()
oper = ("'"+op+"'")
a = int(x)
b = int(y)
res = calculo(oper, a, b)
print(res)
print('example: ', calculo('sum', 36, 9))