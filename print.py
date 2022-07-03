# segundo archivo en Python
a= int (97)
b= float (97)
a = int(b)
print (a,b)
print (a+b-a if b == a else 'no iguales')
print('/\\'*7)

num = 0.97123456789
print(f'Cadena con porcentaje {num:%}')
print(f'Cadena con porcentaje {num:.2%}')

print(f'{num*10000:,.2f}')
print(f'{num*1000000:_.2f}')
print(f'{num*10000000:,.3f}'.replace(',', ' '))
num = 75
print(f'{num:b}')
print(f'{num*10000:.5e}')
print(f'{num*10000:.3E}')
print(f'{num:07}')
print(f'{num:+05}')
print(f'{num:-06}')

print('/\\'*7)

c = "Eddie"
print (c)
print ("-".join(c))
print (c.split())
print (c.replace('E','e'))

print(f'{c:^11}')
print(f'{c:*^11}')
print(f'{c:>11}')
print(f'{c:<11}')
print(f'{{c}} = {c}')

