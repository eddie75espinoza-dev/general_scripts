"""
Ejercicio 2)
Escriba en python un pequeño webserver que funcione como un Apache cuando 
se habilita el directory listing.
Cuando se accede desde un browser debe mostrar la estructura de archivos 
y directorios (desde el directorio actual donde se ejecutó) y permitir 
navegar por los mismos.
Solo se debe usar la standard library de python y no se puede usar el modulo http (C:\>python3 -m http.server o 
c:\python3 -m http.server --bind 127.0.0.1).

Ejemplo:
Directory listing for /
.vscode/
1ejercicio.py
2ejercicio.py
__pycache__/
addprocess.py
anagrams.py
balancedstr.py
bisiesto.py
"""
from distutils import dir_util
import pathlib
import os
from flask import Flask

app = Flask(__name__)



'''
El método absolute() devuelve la ruta completa del archivo, y la función parent() recupera el directorio del archivo a partir de esta ruta.
'''
print(pathlib.Path(__file__).parent.absolute())

'''
Para obtener el directorio de trabajo actual, eliminamos el nombre del fichero de la función anterior.
'''
print(pathlib.Path().absolute()) # 

'''
La función abspath() puede obtener la ruta del archivo requerido, y la función dirname() obtiene el directorio de la ruta completa.
'''
print(os.path.dirname(os.path.abspath(__file__)))

'''
Para obtener el directorio de trabajo actual
'''
print(os.path.abspath(os.getcwd()))

path = 'C:\\Users\\Usuario\\Desktop\\Backup\\Desktop\\Python\\PyGeneral'
for nombre_directorio, dirs, ficheros in os.walk(path, topdown=False):
    print(nombre_directorio)
    for nombre_fichero in ficheros:
        print(nombre_fichero)

@app.route('/')
def home():
    with os.scandir(path) as ficheros:
        for fichero in ficheros:
            print(fichero.name)
    return fichero.name




if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5080, threaded=True, debug=True)
    