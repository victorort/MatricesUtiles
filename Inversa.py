#Calcular la inversa
import numpy as np
from DeterminanteNDimensiones import Determinante,RecortarMatriz
mat=np.random.rand(4,4)
mat_A = [[2,0,1] ,[3,0,0] ,[5,1,1]]
def Transpuesta(mat):
    MatrizCopiada = np.random.rand(len(mat),len(mat))
    for i in range (len(MatrizCopiada)):
        for j in range( len(MatrizCopiada)):
            MatrizCopiada[i][j] = mat[j][i]
    return(MatrizCopiada)
    
    
    
def Adjuntos(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            matrec = RecortarMatriz(mat,i,j)
            mat[i][j] = Determinante(matrec)
    return(mat)
            
def Menores(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i][j] = ((-1)**(i+j+2)) * mat[i][j]
    return(mat)


def Inversa(mat):
    mtranspuesta = Transpuesta(mat)
    madjuntos = Adjuntos(mtranspuesta)
    mmenores = Menores(madjuntos)
    for i in range(len(mat)):
        for j in range(len(mat)):
            mmenores[i][j] = (mmenores[i][j]/Determinante(mat))
    return mmenores
    
    
    
def PrintMatriz(matriz):
    for lista in matriz:
        print(lista)

print(PrintMatriz(Inversa(mat_A)))