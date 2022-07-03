# encuentra el mayor elemento del array
myArray = [13,2,97,4,35,1,75,9,7]

print(sorted(myArray)[-1])

print(max(myArray))
print(min(myArray))


# Otro ejemplo de sorted
scores = {
    'batman': 85,
    'superman': 99,
    'aquaman': 72,
    'spiderman': 91
}

heroes = [
    'batman',
    'superman',
    'aquaman',
    'spiderman'
]

# Ordenar heroes por su score mas alto de mayor a menor
print(sorted(heroes,key=scores.get,reverse=True))