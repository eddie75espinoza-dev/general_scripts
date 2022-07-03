"""
Valida una entrada de numero separados por espacios y determina si se encuentran 
en un rango especifico, a manera de datos de horas
"""
import time

def is_validate_entrance(lst):
    try:
        if len(lst) < 3:
            raise Exception("Enter 3 numbers separated by spaces")
        else:    
            h = lst[0].isnumeric()
            m = lst[1].isnumeric()
            s = lst[2].isnumeric()

        if h: 
            hour = int(lst[0])           
            if hour >= 0 and hour < 24:
                hour = int(lst[0])
            else:
                raise Exception('Enter an hour correct')
        else:
            raise Exception ("Hour -> Only integers")

        if m: 
            minute = int(lst[1])           
            if minute >= 0 and minute < 60:
                minute = int(lst[1])
            else:
                raise Exception('Enter a minute correct')
        else:
            raise Exception ("Minute -> Only integers")

        if s: 
            seconds = int(lst[2])           
            if seconds >= 0 and seconds < 60:
                seconds = int(lst[2])
            else:
                raise Exception('Enter a Seconds correct')
        else:
            raise Exception ("Seconds -> Only integers")

        return [hour, minute, seconds]
    except Exception as e:
        print("Error:", e)

def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

if __name__ == '__main__':
    
    data_in = input("When timer ends? (hour, minute, seconds): ").split(" ")
    print(data_in)
    hms = is_validate_entrance(data_in)
    print(type(hms))
    print(type(hms[0]))
    print(type(hms[1]))
    print(type(hms[2]))
    
    print(segundos_a_segundos_minutos_y_horas(7597))