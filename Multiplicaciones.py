import numpy as np

mat1=[[2,4],[1,2]]
mat2 = [[1,0],[0,1]]

def MultiplicarMatrices(mat1,mat2):
    """
    Calculamos la nueva dimensión de la matriz y vemos si las dimensiones son compaibles
    
    """
    mat3 = np.random.rand(np.shape(mat1)[0],np.shape(mat2)[1])
    
    if np.shape(mat1)[1] != np.shape(mat2)[0]:
        return("Estas matrices no se pueden multiplicar")
    else:
        for fila in range(np.shape(mat1)[0]):
            for columna in range (np.shape(mat2)[1]):
                op = 0
                for elemento in range (np.shape(mat1)[0]):
                    op += mat1[fila][elemento] * mat2[elemento][columna]
                mat3[fila][columna] = op
        return mat3
  
def ElevarMatriz(mat,exponente):
    nmatriz = mat
    for i in range(exponente-1):
        nmatriz = MultiplicarMatrices(nmatriz,mat)
        
    return(nmatriz)
        
            
def PrintMatriz(matriz):
    for lista in matriz:
        print(lista)
  
print(PrintMatriz(MultiplicarMatrices(mat1,mat2)))
print(PrintMatriz(ElevarMatriz(mat1,4)))