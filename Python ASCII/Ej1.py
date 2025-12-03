"""Leer una cadena desde teclado 
y mostrarla carácter por carácter 
usando un ciclo for y el índice"""

cadena = input ("Introduzca su cadena: ") 

for i in range (len(cadena)): 
    print (f"{i}, {cadena[i]}") 

    
#Creamos la variable cadena con un input (Linea 5)
#Creamos un bucle que recorre la cadena y (len(cadena)) cuenta los caracteres (linea 7)
# i muestra el número del caracter y cadena[i] muestra la letra de cada posición (inea 8)