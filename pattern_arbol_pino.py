# -*- coding: utf-8 -*-
#Decoración: Arbol navideño
print()
print('\U0001f332'+"ARBOL NAVIDEÑO".center(15)+'\U0001f332')
print()

import time
count = 1
width = 20
for i in range(10):
    if i == 0:
        print(('\U0001f384'*count).center(width))
    else:
        count += 2
        print(("\u235f"*count).center(width))
        time.sleep(1)
    
print("|   |".center(width))