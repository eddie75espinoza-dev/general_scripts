'''
Character Removal
Have the function CharacterRemoval(strArr) read the array of strings stored in strArr, which will contain 2 elements:
the first element will be a sequence of characters representing a word, and the second element will be a long string
of comma-separated words, in alphabetical order, that represents a dictionary of some arbitrary length. For example:
strArr can be: ["worlcde", "apple,bat,cat,goodbye,hello,yellow,why,world"]. Your goal is to determine the minimum
number of characters, if any, can be removed from the word so that it matches one of the words from the dictionary.
In this case, your program should return 2 because once you remove the characters "c" and "e" you are left with
"world" and that exists within the dictionary.
If the word cannot be found no matter what characters are removed, return -1.
Examples
Input: ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
Output: 4
Input: ["apbpleeeef", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]
Output: 8
'''

def CharacterRemoval(strArr):
    strRes = []
    strIn = strArr[0]
    #print(strIn)
    strMed = ''.join(strArr[1])
    strOut = strMed.split(',')
    #print(strOut)
    if not strIn in strOut:
        return -1
    else:
        for i in strOut:
            if strIn == i:
                strRes.append(i)

    return strRes

print(CharacterRemoval(["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]))
print(CharacterRemoval(["apbpleeeef", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]))

