"""Construir manualmente una nueva cadena añadiendo un carácter a la vez 
(ejemplo: filtrar caracteres o construir cadenas invertidas)."""

#CADENA INVERTIDA

cadena = input("Introduce la cadena: ")
invertida = ""

for caracter in cadena:
    invertida = caracter + invertida
    
print (f"Cadena original: {cadena}")
print (f"Cadena invertida: {invertida}")


#Filtrar Vocales

vocales = ""

for caracter1 in vocales:
    if caracter1.isalpha():
        letra = caracter1.lower()
    
        if letra !="a" or letra !="e" or letra !="i" or letra != "o" or letra !="u":
            vocales += caracter1

print (f"Resultado de vocales: {vocales}")
        