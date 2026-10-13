#Escribir un programa que almacene las matrices
# en una lista y muestre por pantalla su producto.
# matrizA = [[1, 2, 3], [4, 5, 6]]
# matrizB = [[-1, 0], [0, 1], [1,1]]
# Nota: Para representar matrices mediante listas usar listas anidadas, representando 
# cada vector fila en una lista.
import numpy as np

def printMatriz(matriz):
    for columna in matriz:
        for valorfila in columna:
            print(valorfila, end=" ")
        print("\n")

matrizA = [[1, 2, 3], [4, 5, 6]]
matrizB = [[-1, 0], [0, 1], [1,1]]

print("Matriz A")
printMatriz(matrizA)
print("Matriz B")
printMatriz(matrizB)

matrizResult = np.zeros((len(matrizA), len(matrizB[0])))

for i in range(len(matrizA)):
    for j in range(len(matrizB[i])):
        for k in range(len(matrizB)):
            matrizResult[i][j] += matrizA[i][k] * matrizB[k][j]
print("Matriz Resultado")
printMatriz(matrizResult)


