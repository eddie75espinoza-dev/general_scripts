def solution(N):
    N=bin(N)[2:]
    b=0
    maxb=0
    for k in N:
        if int(k) == 0:
            b+=1
        elif int(k) == 1:
            maxb = max(b,maxb)
            b=0
    return maxb


solut = solution(1001101100111) 
print(solut)