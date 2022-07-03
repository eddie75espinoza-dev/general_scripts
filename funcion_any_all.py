# How cool is Python
x = [False, False, False, False]
if any (x):
    print('At least one True')
if not all (x): # se niega y por es true
    print('Not one False')
if any (x) and not all (x):
    print('At least one True and one False')
if any(x) or all (x):
    print('someone True')
else:
    print('every False')