"""Leer una cadena y construir una nueva 
cadena con los caracteres en orden inverso."""

cadena = input("Introduce su cadena: ")
invertida = ""

for i in range (len(cadena)):
    invertida = cadena[i] + invertida
    
print (f"Original: {cadena}")
print (f"Invertida: {invertida}")