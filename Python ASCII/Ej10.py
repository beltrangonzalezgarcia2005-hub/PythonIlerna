"""Leer una cadena y contar cuántos 
caracteres son letras mayúsculas."""

cadena = input("Introduce tu cadena: ")
contador_mayusculas = 0

for i in range (len(cadena)):
    if cadena[i].isupper():
        contador_mayusculas = contador_mayusculas + 1
        
print (f"Su cadena tiene {contador_mayusculas} letras mayúsculas")