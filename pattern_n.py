n = 5
Right = 1
Left = 1
Diagonal = 2

# Main Loop for the rows
for index in range(n):
        
    # For the left Values
    print("\033[6;37;41m"+str(Left)+'\033[0;m', end = "")
    Left += 1
    for side_index in range(0, 2 * (index), 1):
        print(" ", end = "")
    if (index != 0 and index != n - 1):
        print("\033[6;37;41m"+str(Diagonal)+'\033[0;m', end = "")
        Diagonal += 1
    else:
        print(" ", end = "")
    for side_index in range(0, 2 * (n - index - 1), 1):
            print(" ", end = "")
    print("\033[6;37;41m"+str(Right)+'\033[0;m', end = "")
    Right += 1
         
    print("\n", end = "")