# Ejemplo 1
def palindrome1(phrase):    
    phrase2 = phrase[::-1]
    if phrase2 == phrase:
        return True
    return False

#Ejemplo 2
def palindrome2(phrase):    
    return phrase == phrase[::-1]

#ejemplo 3
# frase palindroma: on a clover, if alive, erupts a vast, pure evil; a fire volcano

phrase = input('Indique una palabra o frase palindroma: ').replace(" ", "").replace(",", "").replace(";", "")
isPalindrome = phrase.find(phrase[::-1]) == 0

print("Resultado función 1:", palindrome1(phrase))
print("Resultado función 2:", palindrome2(phrase))
print("Resultado función 3:", isPalindrome)