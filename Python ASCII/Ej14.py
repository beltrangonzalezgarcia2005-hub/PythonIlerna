"""Leer una cadena y contar cuántos
caracteres numéricos ('0' a '9') contiene."""

cadena = input("Introduce su cadena: ")
contador = 0

for i in range (len(cadena)):
    if cadena[i] .isdigit():
        contador = contador+1
 
        
print (f"Cadena original: {cadena}")
print (f"Números dentro de la cadena: {contador}")