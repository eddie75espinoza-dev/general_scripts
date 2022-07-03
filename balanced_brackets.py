# -*- coding: utf-8 -*-
#Decoración: balanced brackets
print("--------------------------------")
print("Balanced Brackets")
print("--------------------------------")
# Function to test balanced brackets
def BalancedBrackets(Str):
    # stack for storing opening brackets
    stack = []
    count = 0
    # Loop for checking string
    for char in Str:

        # if its opening bracket, so push it in the
        # stack
        if char == '(' or char == '[':
            stack.append(char)  # push
        # else if its closing bracket then
        # check if the stack is empty then return false or
        # pop the top most element from the stack
        # and compare it
            count += 1
        elif char == ')' or char == ']':
            count += 1
            if len(stack) == 0:
                return 0
            top_element = stack.pop()
            # pop
            # function to compare whether two
            # brackets are corresponding to each other
            if not Compare(top_element, char):
                return 0

    # lastly, check that stack is empty or not
    if len(stack) != 0:
        return 0


    return 1 , count//2


# Function to check two corresponding brackets
# equal or not.
def Compare(opening, closing):

    if opening == '(' and closing == ')':
        return 1
    if opening == '[' and closing == ']':
        return 1

    return 0

# Test function
print(BalancedBrackets("(123(456[(.768]))"))    #output = 1 4
print(BalancedBrackets("(c([od]er)) b(yt[e])"))  #Output = 1 5
print(BalancedBrackets("(coder)[byte)]"))  #Output = 0