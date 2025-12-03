"""Verificar si un carácter específico 
está en la cadena con un ciclo y comparaciones.
"""

cadena = input("Introduzca la cadena: ")
caracter = input ("Introduzca el caracter a buscar: ")

encontrado = False

for i in range (len(cadena)):
    if cadena[i] == caracter:
        print("Lo encontraste")
        encontrado = True
        break
    else:
        print ("Buscando")
        
print()  
if encontrado:
    print(f"El caracter: {caracter} ha sido encontrado en la cadena {cadena}")
else:
    print(f"El caracter {caracter} no ha sido encontrado en la cadena {cadena}")