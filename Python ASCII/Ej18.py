"""Leer una cadena y construir una nueva cadena
dejando sólo los caracteres que son consonantes 
(sin listas, usando condiciones y concatenación)."""

cadena = input("Introduce tu cadena: ") #Pedimos la variable cadena al usuario
consonantes = "" #Creamos la variable consonante y nop le damos valor

for caracter in cadena: #Hacemos un bucle que recorrera cada caracter de la cadena
    
    if caracter.isalpha(): #Verificamos si el caracter es una letra
        letra = caracter.lower() #Convertimos todas las letras a minusculas para que nos resulte mas facil
        
        if letra !="a" and letra !="e" and letra !="i" and letra != "o"and letra !="u": #Verificamos que la letra no sea una vocal
            consonantes += caracter #Si no es vocal es consonante y la añadimos al resultado
            
print(f"Cadena original: {cadena}")  #Printeamos la cadena original
print (f"Cadena consonantes: {consonantes}") #Printeamos la cadena solo con las consonantes