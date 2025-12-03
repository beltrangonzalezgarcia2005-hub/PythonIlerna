"""Construir una nueva cadena con todos los 
caracteres de la cadena original, pero duplicando 
cada vocal."""

cadena = input("Introduce una cadena: ")
nueva_cadena = ""

for i in range (len(cadena)):
    if cadena[i] in "aeiouAeiou":
        nueva_cadena = nueva_cadena + cadena[i] + cadena[i]
    else:
        nueva_cadena = nueva_cadena + cadena[i]
        
        
print (f"Cadena original: {cadena}")
print (f"Cadena nueva = {nueva_cadena}")
