"""Imprime una estrella de ocho puntas 
combinando líneas verticales, horizontales y 
diagonales con asteriscos en una matriz de tamaño 
impar n x n (ej. 9x9).
Figura para n=9:"""

#Tengamos en cuenta que para realizar figuras ASCII tenemos que utilizar Matrices

n = 9 #Definimos la matriz a 9

centro = n // 2 #Calculamos el centro de la matriz (// significa división sin decimales por lo tanto = 4)

for i in range (n): #Bucle que recorre las filas de la matriz
    for j in range (n): #Bucle que recoore las columnas de la matriz
    
        if i == centro: #Si estamos en la línea del centro imprime "*"
            print("*", end= " ")
        
        elif j == centro: #Si estamos en la columna del medio imprime"*"
            print("*", end= " ")
        
        elif i == j: #Si la fila es igual a la columna imprime "*" Diagonal izq
            print("*", end= " ")
            
        elif i + j == n - 1: #Si i + j = n-1 (8) imprime "*"
            print ("*", end= " ")
        else: #Si no se cumple nada de lo anterior imprimimos " "
            print (" ", end= " ")
    print() #Este print hace un salto de línea después de cada fila
