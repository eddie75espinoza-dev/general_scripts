n = 5

i=1
for j in range (1,i+1):
    print ("<\>", end = "")
    for i in range (n,0,-1):
        for j in range(0,i-1):
            print("<\>", end="")
        print(" ")