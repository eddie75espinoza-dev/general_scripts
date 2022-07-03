# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:00:00 2021

@author: eddie75
"""
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
hora = hora / 60
#durat = dura + min
duramod = (dura + min) % 60
durares = dura / 59
horafin = (hora*60) + durares
horadia = horafin // 24
if horafin >= 23:
    horafin = horafin - 24
    if horafin >= 24:
        horafin = horafin - 24        
        print("El evento dura mas de un dia: ",int(horadia)) 
print('El evento debe culminar a las: {:02d}: {:02d} horas'.format(int(horafin), int(duramod)))