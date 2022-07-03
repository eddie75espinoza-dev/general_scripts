def calculo (op, a, b):
    return {
         'sum': a+b,
         'res': a-b,
         'mult': a*b,
         'div': a/b
    }.get(op)
a = int(input("indique un numero: "))
b = int(input("ingrese un valor : "))
op = input("tipo operacion (sum, res, mult, div): ")
print(calculo(op,a,b))

def calculo2 (op, a, b):
    return {
         'sum': lambda: a+b,
         'res': lambda: a-b,
         'mult': lambda: a*b,
         'div': lambda: a/b
    }.get(op, lambda: None)()

print("Resultado 'sum': ", calculo2('sum',a,b))
print(calculo(input("Nueva operacion (sum, res, mult, div): "),a,b))
