# valida si una palabra es un anagrama
# ejemplos: (alegan, angela), (valora, alvaro), (colinas, nicolas)
# (prisa, paris), (poder, pedro), (ironicamente, renacimiento)

def is_anagram(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    else:
        for i, j in zip(string_1, string_2): # esto ejecuta la verificacion del string           
            if i != j:
                return False
        return True
 
string_1 = input('Firts word: ') # 
string_2 = input("Second Word: ") # 

string_1 = sorted(string_1.lower()) # convierte en lista la cadena
string_2 = sorted(string_2.lower())
print()

# llamando a la funcion
print("Is Anagram" if is_anagram(string_1, string_2) else "Not Anagram")

# Otra forma
print("Anagram List" if string_1 == string_2 else "Not Anagram List")

#===================================================

def check_if_anagram (first_word, second_word): 
    first_word = first_word.lower () #esto se puede validar fuera de la funcion
    second_word = second_word.lower () 
    return sorted (first_word) == sorted (second_word) # metodo sorted() convierte en lista y ordena

print()
print (check_if_anagram ("testinG", "Testing")) # True 
print (check_if_anagram ("Here", "Rehe")) # True 
print (check_if_anagram ("Know", "Now")) # False

#=======================================================

from collections import Counter

def check_if_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    return Counter(first_string) == Counter(second_string)


print(check_if_anagram('testinG', 'Testing'))  # True
print(check_if_anagram('Here', 'Rehe'))  # True
print(check_if_anagram('Know', 'Now'))  # False