# Pattern in V

def pattern(n):
 
    i = n - 1
    j = 1
    for i in range(n - 1, -1, -1):
 
        # outer gap loop
        for j in range(n - 1, i, -1):
            print(' ', end = '')
             
        # 65 is ASCII of 'A'
        print('V', end = '')
 
        # inner gap loop
        for j in range(1, i * 2):
            print(' ', end = '')
 
        if (i >= 1):
            print('V', end = '')
        print()

n = 5

pattern(n)