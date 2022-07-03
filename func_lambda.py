def multiplicar_por (n):
  return lambda x: x * n
  
duplicar = multiplicar_por(2)
triplicar = multiplicar_por(3)
diez_veces = multiplicar_por(10)

print(duplicar(4))
print(triplicar(3))
print(diez_veces(5))
print(multiplicar_por(8)(2))

# factorial

fact = lambda n:[1,0][n>1] or fact(n-1)*n   # <--

print(fact(7))

# fibonacci

fib = lambda x:x if x<=1 else fib(x-1) + fib(x-2)   # <--

print(fib(16))