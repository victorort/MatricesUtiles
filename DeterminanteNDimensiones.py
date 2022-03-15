import numpy as np



mat_A=[   [1,2,18,4,1,0 ]    ,  [0,1,1,1,5,11] , [ 1,1,2,1,5,-4]  ,[1,2,2,3,5,3],[1,2,18,4,5,2],[1,1,3,4,1,0]]

def Determinante(mat_A,ntotal =0):
    
    if len (mat_A)==2:
        valor=mat_A[0][0] * mat_A[1][1] - mat_A[1][0] * mat_A[0][1]
        return valor
    else: 
        #REGLA DE LA PLACE, SE VAN ELIMINADO COLUMNAS Y LA FILA 1 Y SE HACE LA OPERACION(adjunto)    
        for j in range(len(mat_A)):
            nMatriz = RecortarMatriz(mat_A,0,j)    
            suma= mat_A[0][j] * ((-1)**(2+j)) 
            ntotal += suma  * Determinante(nMatriz)
        return ntotal
            
    
def RecortarMatriz(matriz, i,j):
    #Recorta la matriz eliminado la fila uno y las columnas van cambiando
    matriz1 = np.delete(matriz, [i], axis = 0)
    matriz2 = np.delete(matriz1, [j] , axis = 1)
    matriz = matriz2
    return matriz

"""    
def PrintMatriz(matriz):
    for lista in matriz:
        print(lista)
"""
print(Determinante(mat_A))
print(np.linalg.det(mat_A))