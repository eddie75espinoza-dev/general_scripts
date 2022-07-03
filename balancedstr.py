'''
Multiple Brackets
Have the function MultipleBrackets(str) take the str parameter being passed and return 1 #ofBrackets if the brackets are
 correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello [world])(!)", then
 the output should be 1 3 because all the brackets are matched and there are 3 pairs of brackets, but if str is
 "((hello [world])" the the output should be 0 because the brackets do not correctly match up.
 Only "(", ")", "[", and "]" will be used as brackets. If str contains no brackets return 1.
Examples
Input: "(coder)[byte)]"
Output: 0
Input: "(c([od]er)) b(yt[e])"
Output: 1 5
Browse Resources
Search for any help or documentation you might need for this problem. For example:
array indexing, Ruby hash tables, etc.

'''


def BalancedBrackets(strParam):
    stack = []    
    count = 0
    for char in strParam:

        if char == '(' or char == '[':
            stack.append(char)
            count += 1
        elif char == ')' or char == ']':
            count += 1
            if len(stack) == 0:
                return False
            top_elem = stack.pop()
            if not Compare(top_elem, char):
                return False

        # lastly, check that stack is empty or not
    if len(stack) != 0:
        return False
    count = str(' ' + str(count // 2))
    strParam = str('1' + count)
    return strParam #true


# Function to check two corresponding brackets
# equal or not.
def Compare(opening, closing):
    if opening == '(' and closing == ')':
        return 1
    if opening == '[' and closing == ']':
        return 1
    return False

# Test function
print(BalancedBrackets("(123(456[().768]))"))    #con STRPARAM output = 1 4
print(BalancedBrackets("(T([ru]e)) b(yt[e])"))  #Output = 1 5
print(BalancedBrackets("(True)[(byte)]"))  #Output = 1 3 # True
print(BalancedBrackets('(True)')) #True
print(BalancedBrackets('(F)a]l[s(e)')) # False
print(BalancedBrackets('Fal(se')) # False
print(BalancedBrackets('([(Fa]l)se)')) # False