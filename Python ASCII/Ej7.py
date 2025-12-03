"""Reemplazar un carácter por otro recorriendo 
la cadena y concatenando a una nueva cadena."""

cadena = input ("Introduce tu cadena: ")
c_viejo = input("Que caracter desea reemplazar?: ")
c_nuevo = input("Que caracter desea añadir?: ")

cadena_nueva= " "

for i in range (len(cadena)):
    if cadena[i]== c_viejo:
        cadena_nueva = cadena_nueva + c_nuevo
        print(f"Posición {i}: {cadena[i]}, reemplazado por: {c_nuevo} --> {cadena_nueva}")
    
    else:
        cadena_nueva = cadena_nueva + cadena[i]
        print(f"Posición {i}: '{cadena[i]}' → se mantiene → '{nueva_cadena}'")

print(f"Cadena original: {cadena}")
print(f"Cadena modificada: {cadena_nueva}")

#REPETIR