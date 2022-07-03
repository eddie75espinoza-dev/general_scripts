#!/bin/python3
'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1


 and  is even, so it is not weird.
'''

import math
import os
import random
import re
import sys


n = int(input().strip())
if n >=1 and n<=100:    
    if n>=2 and n<=5: 
        if n % 2 ==0:     
            print('Not Weird') #2,4
        else:
            print('Weird') #3,5
    elif n>=6 and n <=20:
        if n % 2 == 0:
            print('Weird') #6,8,20
        else:
            print('Not Weird') #7,19
    else:
        if n % 2 == 0:
            print('Not Weird') # 22, 24
        else:
            print('Weird')   # 21, 29
else:
    print('Weird') #100, 1

#Otra forma mas simple

n = int(input().strip())

if n % 2 == 1:
    print("weird")
elif n < 5:
    print("Not Weird")
elif n <= 20:
    print("weird")
else:
    print("Not Weird")