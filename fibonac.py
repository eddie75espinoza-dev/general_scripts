# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 15:54:11 2021

@author: Eddie75
"""

# funcion fibonacci entre 0 y num
#solucion 1 Funcion muy lenta

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return (fibonacci(num - 1) + fibonacci(num - 2))

#solucion 2 funcion mas rapida
fibo = lambda num, x=[0,1]: x if len(x) == num else fibo(num, x+[sum(x[-2:])])

n = 30

print(fibo(n),'\n')
print('Num Seq')
for n in range(n):
    print(n, " ", fibonacci(n))


# solucion 3 

fib = lambda x:x if x<=1 else fib(x-1) + fib(x-2)   # <--

print(fib(29))