''' Obtener una numero de dia del año
Escenario
Tu tarea es escribir y probar una función que toma tres argumentos 
(un año, un mes y un día del mes) y devuelve el día correspondiente 
del año, o devuelve None si cualquiera de los argumentos no es válido.
'''
#codigo
def isYearLeap(year):
    if year % 400 == 0:
       return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
    return

def daysInMonth(year, month):
    daysMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = []
    day=0
    if isYearLeap(year):
        daysMonth[1] = 29
    
    for i in range (0,month-1):
        days = daysMonth[i]
        day += days
        
    return day

def dayOfYear(year, month, day):
    parcial = daysInMonth(year, month)+day
    return parcial

print(dayOfYear(2000, 12, 31))

## salida : 366
