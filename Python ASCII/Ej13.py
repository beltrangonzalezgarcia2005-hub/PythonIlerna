"""Leer una cadena y eliminar todos los 
espacios, construyendo una cadena continua."""

cadena = input ("Introduce una cadena:")
cadena_nueva = ""

for i in range (len(cadena)):
    if cadena[i] != " ":
        cadena_nueva = cadena_nueva + cadena[i]
        
print (f"Cadena original: {cadena}")
print (f"Cadena sin espacios: {cadena_nueva}")