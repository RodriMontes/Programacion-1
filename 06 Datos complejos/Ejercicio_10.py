# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 
# Ejemplo:

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario invertido:", capitales)