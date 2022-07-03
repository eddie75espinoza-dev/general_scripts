# to swap variables

a = 7
b = 9
print(a, b)
a, b = b, a # <--
print(a, b)

# reverse a string

_str = "reversed"
print(_str)
print(_str[::-1])   # <--

# string palindrome

my_str = "arepera"
palin = my_str == my_str[::-1]  # <--

print(palin)

# factorial

fact = lambda n:[1,0][n>1] or fact(n-1)*n   # <--

print(fact(7))

# fibonacci

fib = lambda x:x if x<=1 else fib(x-1) + fib(x-2)   # <--

print(fib(16))