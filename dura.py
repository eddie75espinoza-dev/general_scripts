def stair_case(n):
    for i in range(n):
        print(" " * (n-1-i), end="")
        print("#" * (i+1))

def StayAtHome():
    print("#QuedateEnCasa ; ", "#Bleib Zu Hause ; ", "#Restez a la maison ; ","#Resta A casa ; ""#StayAtHome\n")
n = int(input("Lineas?: "))
stair_case(n)
for x in range (n):
    x+=1
    n-=1-x
    StayAtHome()



  


