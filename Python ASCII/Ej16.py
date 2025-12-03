"""Leer dos cadenas y concatenarlas manualmente 
sin usar el operador + en una sola operación 
(concatenar carácter a carácter con un ciclo)."""

cadena1 = input("Introduce la cadena1: ")
cadena2 = input("Introduce la cadena2: ")
fusion = ""

for i in range (len(cadena1)):
    fusion = fusion + cadena1[i]
    
for i in range (len(cadena2)):
    fusion = fusion + cadena2[i]
    
print (f"Cadena fusionada: {fusion}")