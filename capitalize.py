myStr = input('Indica palabra a capitalizar: ')

def solve(myStr):
    for x in myStr[:].split():
        print(x)
        myStr = myStr.replace(x, x.capitalize())
    return myStr
    
print(solve(myStr))

print(myStr.capitalize())