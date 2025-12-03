"""Imprime un diamante hueco de altura total 
2n - 1,centrado con asteriscos, donde solo se 
imprimen los bordes y el centro.
Figura para n=5:"""

n = int (input("Introduce el valor de n: "))
    
for i in range (n):
    hueco_ext = n - i - 1
        
    if i == 0:
        print (" " * hueco_ext + "*")
    else:
        hueco_int = 2 * i - 1
        print (" " * hueco_ext + "*" + " " * hueco_int + "*")
        
for i in range (n-2, -1, -1):
    hueco_ext = n - i - 1
        
    if i == 0:
        print (" " * hueco_ext + "*")
    else:
        hueco_int = 2 * i - 1
        print (" " * hueco_ext + "*" + " " * hueco_int + "*")