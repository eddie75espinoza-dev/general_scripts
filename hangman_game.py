"""
# The Hangman Game

## Juego desarrollado con Python para usar en consola

Esta version muestra el manejo de coordenadas en la consola y el uso de sombreado 
sobre los mensajes de salida, asi como el uso de caracteres especiales,
hace uso del posicionamiento del cursor para mostrar el juego sin un scroll de la consola.

Manejo de iterador

dev: Eddie75Espinoza
date: 26/2/2022
"""

import time
import random

words = ['act', 'cat', 'brag', 'cider', 'cried', 'dog', 'god', 'dusty', 'study', 'night', 'thing', 'peach', 'cheap', 'players', 'parsley', 'state', 'taste', 'aeronautism', 'anemious', 'aeroacoustic']

hangman_graphics = [
    "\033[5;32m"+'_',
    "\033[5;32m"+'__',
    '\033[5;32m'+'__\n |',
    '\033[5;36m'+'__\n |\n \u2368',
    '\033[5;36m'+'__\n |\n \u2368\n |',
    "\033[5;33m"+'__\n |\n \u2368\n/|\n',
    "\033[5;33m"+'__\n |\n \u2368\n/|\ \n\n',
    '\033[5;31m'+'__\n |\n \u2368\n/|\ \n/\n\n',
    '\033[5;31m'+'__\n |\n \u235f\n/|\ \n/ \ \n'
]
def draw(lst,n, d=0):
    """ iterador para dibujar el hangman graphic"""
    for i in range(d, len(lst), n):
        print("\033[1;1f")     # limpia la consola para mostrar el dibujo en la misma posicion   
        yield print(lst[i+n])

mistakes = 0
letters_guessed = []
mistakes_allowed = 8 #len(hangman_graphics)
word = random.choice(words)
letters_word = list(word)
wrong_letters = []


while mistakes < mistakes_allowed:
    print('\n'*(mistakes_allowed-mistakes)) # ubicacion sin el uso de las coordenadas de consola
    print('\033[14;1f'+f'The word has {len(letters_word)} letters')
    print('Wrong letters: ', end='')
    for letter in wrong_letters:
        print(f'{letter}', end='')
    print(f'\nGuesses left: {mistakes_allowed-mistakes}') # diferencia de errores
    letter_user = input('\033[17;1f''Enter a letter --> ')
    while letter_user in letters_guessed or letter_user in wrong_letters:
        """ valida que la letra ya se haya usado """
        #mistakes += 1 
        #print('\033[16;1f'+f'\nGuesses left: {mistakes_allowed-mistakes}')
        print('You have already entered this letter, enter another one')
        letter_user = input('\033[17;1f'+'Enter a letter --> ')

    if letter_user not in letters_word:
        mistakes += 1   # incrementa el contador de error
        print("\033[1;1f")  # devuelve el cursor a la primera fila y columna
        next(draw(hangman_graphics, mistakes)) # iterador para mostrar el hangman graphics
        wrong_letters.append(letter_user)
        if mistakes == mistakes_allowed:
            print("\033[2J\033[1;1f") # Borra pantalla y situa el cursor en la consola
            next(draw(hangman_graphics, 8)) # uso de iterador
            time.sleep(1)
            print('\033[6;37;41m'+'GAME OVER...\nYou Lost! Try again'+'\033[0;m') # texto color blanco sobre fondo rojo
            print()   
            break

    print('\033[13;1f'+'Word: ', end='') # posiciona el print sobre una ubicacion XY de la consola

    for letter in letters_word:
        if letter_user == letter:
            letters_guessed.append(letter_user)

    for letter in letters_word:
        if letter in letters_guessed:
            print(f'{letter} ', end='')
        else:
            print('_ ', end='')
        

    if len(letters_guessed) == len(letters_word):
        print("\033[2J\033[1;1f"+"\n\x1b[0;32;44m"+"You Wooooon!!!!".center(30)) # texto blanco sobre fondo azul
        print('\033[0;37;40m') # devuelve el formato original a la consola
        break