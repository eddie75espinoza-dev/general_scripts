
def number_format(n1=0, n2=0):
    total = n1 + n2
    print("formato numerico #,###.##")
    return print(f'{total:,.2f}') # se da formato americano de , y 2 decimales al precio

if __name__ == '__main__':
    n1 = float(input('Indica un 1` numero: ').strip())
    n2 = float(input('Indica un 2` numero: ').strip())

    number_format(n1, n2)