"""
Este ejercicio permite encontrar las palabras de un texto segun la cantidad de letras que se soliciten

Texto: "relativamente nuevo en Python"
Input > 13

Output  >   relativamente

"""

def find_string(text, large) -> None:
    """ Funcion para extraer las palabras 
        de un texto dado segun la cantidad
        de letras solicitas
    """
    line = round(len(text)/large)
    textListLine = []
    textList = text.split()
    for txt in textList:
        txtLen = len(txt)
        for linetxt in range(line):
            if txtLen == large:
                print(txt, end="\n")
                break
            textListLine.append(linetxt)


if __name__ == '__main__':
    myText = "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera."
    print("Funcion para extraer las palabras de un texto dado segun la cantidad de letras solicitas")
    large_String = int(input("Indique la cantidad de letras: "))

    find_string(myText, large_String)