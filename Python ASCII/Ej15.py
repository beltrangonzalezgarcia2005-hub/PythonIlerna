"""Dada una cadena, construir una nueva cadena
donde cada vocal se reemplaza por un asterisco
'*'."""

cadena = input("Introduce una cadena de texto: ")
asterisco = ""

for i in range (len(cadena)):
    if cadena[i] in "AEIOUaeiou": #Cadena[i] representa cada caracter de la cadena
        asterisco = asterisco + "*" #Asterisco esta vacío por lo que se le añade a su calor un *
    else:
        asterisco = asterisco + cadena[i] #A asterisco se le añade el caracter original

print (f"Cadena original: {cadena}")
print(f"Cadena con asteriscos: {asterisco}")