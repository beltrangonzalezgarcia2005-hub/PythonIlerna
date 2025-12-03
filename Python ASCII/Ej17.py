"""Leer una cadena y crear una nueva
donde sólo aparezcan los caracteres 
que se repiten más de una vez."""

cadena = input("Introduzca su cadena: ")

frecuencia = {} #Crea un diccionario vacío llamado frecuencia donde guardamos cuántas veces aparece cada carácter.

for caracter in cadena: #Bucle que recorre cada caracter
    frecuencia[caracter] = frecuencia.get(caracter, 0) + 1 #Busca el caracter en el diccionario y si existe devuelve el valor, si no devuelve 0
    
resultado= "" #creamos una cadena vacia para guardar el resultado
vistos = set()  #Creamos un conjunto vacío para guardar que caracter hemos visto ya

for caracter in cadena: #Volvemos a recorrer cada caracter de la cadena
    if frecuencia [caracter] > 1 and caracter not in vistos: #Si el caracter sale mas de una vez y no esta en vistos
        resultado += caracter #Añadimos el caracter a la cadena
        vistos.add(caracter) #Añadimos el caracter al conjunto
        
print (f"Cadena original: {cadena}") #Printeamos la primera cadena
print (f"Cadena nueva: {resultado}") #Printeamos la cadena nueva {resultado}