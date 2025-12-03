"""Imprime un rombo sólido de altura
2n-1, centrado, usando asteriscos.
Figura para n=4:"""

n = 4

for i in range (n):
    for j in range (n -i -1):
        print(" ", end="")
        
    for j in range (2*i+1):
        print("*",end="")
    print()
    
for i in range (n-2, -1, -1):
    for j in range (n -i -1):
        print(" ", end="")
        
    for j in range (2*i+1):
        print("*",end="")
    print()