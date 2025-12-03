"""Imprime la letra M mayúscula usando 
asteriscos en una matriz cuadrada de tamaño 
impar n. Las líneas de la M deben visualizarse 
usando asteriscos, con espacios en el resto.
Figura para n=7:"""

n = 7

for i in range (n):
    linea =""
    for j in range (n):
        laterales = (j == 0) or (j == n-1)
        d_izq = (i == j) and (i<= n//2)
        d_der = (j == n - (i+1)) and (i <= n//2)
        
        if laterales or d_izq or d_der:
            linea += "*"
        else:
            linea +=" "
    print(linea)