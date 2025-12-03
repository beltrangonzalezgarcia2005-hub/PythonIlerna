"""Convertir todas las letras a mayúsculas o minúsculas 
usando ciclos y sumas de caracteres 
(sin usar los métodos upper() o lower())."""

#Cadena a Mayúsculas
cadena = input("Introduce tu cadena minuscula: ")
mayuscula = ""

for i in range (len(cadena)):
    caracter = cadena[i]
    
    if "a" <= caracter <= "z":
        mayuscula = mayuscula + chr(ord(caracter) - 32)
        
    else:
        mayuscula = mayuscula + caracter
    
print (f"cadena original: {cadena}")
print (f"cadena mayúscula: {mayuscula}")


#Cadena a minúsculas
cadena1 = input("Introduce tu cadena mayuscula: ")
minuscula = ""

for i in range (len(cadena1)):
    caracter1 = cadena1[i]
    
    if "A" <= caracter1 <= "Z":
        minuscula = minuscula + chr(ord(caracter1) + 32)
        
    else:
        minuscula = minuscula + caracter1
    
print (f"cadena original: {cadena1}")
print (f"cadena mayúscula: {minuscula}")