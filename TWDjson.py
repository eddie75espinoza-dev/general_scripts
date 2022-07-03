#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Fecha 01/01/2022

Lee un archivo JSON. Data relacionada a la serie THE WALKING DEAD
"""

import json

with open('TWD.json', "r") as TWD:
    wd = json.load(TWD)
    print(wd["serie"])
    print(wd["years"])
    print(wd["genre"])
    print(wd["seasons"][0].get('episode')[0].get('epilogue'))   # Episodio 1 temporada 1
    #print(wd["seasons"][1].get('episode')[0].get('epilogue'))   # Episodio 1 temporada 2
    print("*-/| TWD |\-*"*3)
    print(wd["characters"][0].get('name'))   # Personajes
    print(wd["characters"][5].get('name'))   # Personajes
    print(wd["characters"][7].get('name'))   # Personajes
    print("*-/|\-"*3)
    #print(wd['characters'])
