# muestra un mes en la terminal
import calendar

calendar.setfirstweekday(calendar.SUNDAY)

year = int(input("Year (yyyy): "))
month = int(input("Month (mm): "))

_calendar = calendar.monthcalendar(year, month)

print("=:="*10)
print(calendar.month(year, month))
print("=:="*10)
print(_calendar)
print("=:="*10)
week = int(input("Week: "))-1
_day = int(input("Day: "))-1
dating = _calendar[week][_day]
print('{:>3}: {:>2}'.format(calendar.month_abbr[month],
                                dating))


# imprime el año completo
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatyear(year, 2, 1, 1, 3))

today = calendar.weekday(2022, 2, 2)
day_dict = {
    0: 'sunday',
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday'
}
print("2022/02/feb It is", day_dict[today])