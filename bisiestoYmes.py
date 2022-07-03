''' Años y dias de mes
Escenario
Tu tarea es escribir y probar una función que toma dos argumentos
(un año y un mes) y devuelve el número de días del mes/año dado
(mientras que solo febrero es sensible al valor year, tu función 
debería ser universal).

La parte inicial de la función está lista. Ahora, haz que la función 
devuelva None si los argumentos no tienen sentido.
'''
#year = int(input('Indica un a#o: '))
def is_year_leap(year):
    if year % 400 == 0:
       return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
    return

def days_in_month(year, month):

    daysMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = []
    
    if is_year_leap(year):
        daysMonth[1] = 29
    
    for i in range (0,month):
        days = daysMonth[i]
        
    return days

testYears = [1900, 2000, 2016, 1987,2020]
testMonths = [2, 2, 1, 11,9]
testResults = [28, 29, 31, 30,30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

'''
salida
1900 2 ->OK
2000 2 ->OK
2016 1 ->OK
1987 11 ->OK
2020 9 ->OK
'''