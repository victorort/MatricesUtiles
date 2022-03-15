import numpy
import os
import time


from DeterminanteNDimensiones import Determinante, RecortarMatriz
from Inversa import *
from Multiplicaciones import *

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


print("PROGRAMA MATRICES UTILES\n")
print("1.Determinante")
print("2.Inversa")
print("3.Multiplicar 2 Matrices")
print("4.Elevar una Matriz\n")


Seleccion = int(input("Escribe la opcion que quieres realizar(escribe el número"))