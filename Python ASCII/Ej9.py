"""Leer una cadena y contar 
cuántas vocales contiene."""

cadena = input("Introduce tu cadena: ")
vocales = 0

for i in range (len(cadena)):
    if cadena[i] in "AEIOUaeiou":
        vocales = vocales + 1
        
print (f"La cadena: {cadena}, contiene {vocales} vocales")