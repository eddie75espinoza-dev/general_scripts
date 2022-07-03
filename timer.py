"""
# Temporizador

## Script en Python para representar un temporizador

Temporizador con notificacion nativa (windows), permite validar la entrada
de datos.

Entrada:
When timer ends? (hour, minute, seconds): 1 1 3

Salida:
Hour: 01, Minute: 01, Minute: 03
01:01:03
...
00:01    stop
(Notificacion)

Dev: Eddie75Espinoza
date: 01/03/2022
"""

import time
from pynotifier import Notification

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

def conver_to_seconds(lst):
    total_sec = lst[0]*3600 + lst[1]*60 + lst[2]
    return total_sec

def send_notification():
    Notification(
        title = "Timer",
        description = "The time is finished!",
        icon_path = None,#"C:\\Users\\Usuario\\Desktop\\Backup\\Desktop\\Python\\PyGeneral\\Iconarchive-Red-Orb-Alphabet-Letter-E.ico", #https://iconarchive.com/show/red-orb-alphabet-icons-by-iconarchive/Letter-E-icon.html
        duration = 7,
        urgency = "normal"
    ).send()

def countdown(time_sec):
    while time_sec:
        if time_sec < 60:
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            time_sec -= 1
        else:
            hour = int(time_sec / 3600)
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}:{:02d}'.format(hour, mins if mins< 60 else mins-60, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            time_sec -= 1
    print("\033[1;33m"+"\t stop"+"\033[0;37m") # salida en amarillo + reset de texto


if __name__ == '__main__':
    try:
        data_in = input("When timer ends? (hour, minute, seconds): ").split(" ")
        hms = is_validate_entrance(data_in)
        
        print("Hour: " + str(hms[0]).zfill(2) + \
            ", Minute: " + str(hms[1]).zfill(2) + \
            ", Minute: " + str(hms[2]).zfill(2))
        
        countdown(conver_to_seconds(hms))
        
        send_notification()
    except Exception as e:
        print("Error:", e)

