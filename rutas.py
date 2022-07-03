"""
The anatomy of a PosixPath

PosixPath(\\Users\\Usuario\\Desktop\\Backup\\Desktop\\Python\\PyGeneral)
"""
from pathlib import Path, PosixPath
import pathlib

path = Path(r'C:/Users//Usuario//Desktop//Backup//Desktop//Python//PyGeneral//arbol_pino.py')

print(f'>>> ruta: {path}')
print(f'path.drive    : {str(path.drive)}')
print(f'path.root     : {path.root}')
print(f'path.anchor   : {path.anchor}')
print(f'path.parent   : {path.parent}')
print(f'path.stem     : {path.stem}')
print(f'path.suffix   : {path.suffix}')
print(f'path.suffixes : {path.suffixes}')
print(f'path.parts    : {path.parts}')
print(f'path.name     : {path.name}')
print()
print(repr(path))
print()
print(f'Current directory{Path.cwd()}')
print()
import shutil
root = path
print(root.exists())
print(shutil.get_terminal_size())
print()
with path.open() as f:
    lines = f.readlines()

print(lines)
print()

