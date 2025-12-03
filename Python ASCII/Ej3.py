"""Contar cuántas veces aparece un carácter 
dado en una cadena usando for y un contador"""

cadena = input("Introduzca su cadena: ") #Definimos cadena con un input
caracter = input ("Ingresa el caracter a buscar: ") #definimos el caracter a buscar como input

contador = 0 #creamos la variable contador y la igualamos a 0

for i in range (len(cadena)): #El bucle recorre cada posición de la cadena
    if cadena [i] == caracter: #Preguntamos si el caracter que buscamos esta en esa posición
        contador = contador + 1 # Cada vez que encontremos el caracter el contador aumenta 1
        
print(f"El carácter {caracter} aparece {contador} veces")