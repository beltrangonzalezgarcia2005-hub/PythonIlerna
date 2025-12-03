"""Imprime una pirámide de altura n 
donde se alternan asteriscos y espacios, 
formando un patrón de huecos internos.
Figura para n=6:"""

n = 6 #Definimos el tamaño de la matriz
for i in range(n): #Bucle que recorre las filas de la matriz
   
    espacios_izq = n - i - 1 #Calculamos los espacios antes del primer "*" para centrar la figura
    print(' ' * espacios_izq, end='')
    
   
    ancho = 2 * i + 1 #Calculamos cuantos espacios debe tener cada fila
   
    
    if i == 0: #Primera fila
        print('*', end='')
   
    elif i == n - 1: #Última fila
        print('*' * ancho, end='')
  
    elif i == 3: #Fila central donde agregamos los demás "*"
        
        for j in range(ancho): #Bucle que recorre las columnas de la matriz
            if j % 2 == 0: #Si la posición es par imprime "*"
                print('*', end='')
            else: #Si la posición es impar imprime un espacio 
                print(' ', end='')
  
    else: #Filas 1,2,4
        for j in range(ancho): #Imprimimos solo los bordes
            if j == 0 or j == ancho - 1: #j==0 (bordes izq) // j==ancho - 1 (bordes der)
                print('*', end='')
            else: #Cualquier otra posición imprime espacios
                print(' ', end='')
    
    print() #Salto de línea después de cada fila