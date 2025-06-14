#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra. 


# Pedimos la frase al usuario
frase = input("Ingrese una frase: ")

# Convertimos la frase en una lista de palabras

palabras = frase.lower().split()
palabras_unicas = set(palabras)

# Creamos un diccionario para contar las palabras

frecuencia = {}

# Contamos las palabras

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", frecuencia)