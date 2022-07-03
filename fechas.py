# Libreria HOLIDAYS permite verificar 
import time
from datetime import date
import holidays

# holidays
arg_holidays = holidays.Argentina()

today = time.strftime('%Y-%m-%d')
print("Today is ", today)

today2 = time.strftime('%d/%m/%Y')
print ('Second option: ', today2)

print()

# imprime todos los dias del a;o
""" for date, name in sorted(holidays.ARG(years=2021).items()):
    print(date, '==>', name)
 """

_year, _month, _day = input('Indique una fecha feriada YYYY MM DD: ').split()

print()
print(f'En la fecha {_year}/{_month}/{_day} se celebra o conmemora: ', end="")
#Regresa el parametro correspondiente a la fecha
print(arg_holidays.get(date(int(_year), int(_month), int(_day))))
#Regresa el parametro correspondiente a la fecha (Otra forma)
print(arg_holidays[date(int(_year), int(_month), int(_day))])