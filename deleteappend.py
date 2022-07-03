'''

'''
import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    o = t.lower()
    p = s.lower()
    a = list(p)
    b = list(o)
    print(a)
    print(b)
    r=[]
    for i in range(len(a), k, -1):
        del(a[k:len(a)-i-1])
        r = a
    for i in range(len(b)):
        del(b[len(b)-i-1 ])
        r.append(b[i])

    str1 = ''.join(r)
    return str1

if __name__ == '__main__':

    s = input('palabra 1: ')

    t = input('palabra 2: ')

    k = int(input())
    if 1 <= k <= 100 and 1 <= len(s) <= 100 and 1 <= len(t) <= 100:
        result = appendAndDelete(s, t, k)

    print(result)

