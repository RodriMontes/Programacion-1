# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

#Agregamos nuevas frutas

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 

# Solo las frutas, sin los precios

list_frutas = list(precios_frutas.keys()    )
print(list_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 
# Ejemplo:
 
#cargamos 5 contactos
agenda = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    agenda[nombre] = numero

# Consultamos un contacto

consulta = input("Ingrese el nombre del contacto a consultar: ")

if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("El contacto no existe en la agenda")
    
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


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingresá nota {j+1} de {nombre}: ")) for j in range(3))
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 

stock = {
    "arroz": 10,
    "leche": 5,
    "pan": 20
}

producto = input("Ingresá el nombre del producto: ")

if producto in stock:
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto nuevo. Ingresá stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora. 

agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "14:00"): "Clase de programación"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato hh:mm): ")

clave = (dia, hora)
if clave in agenda:
    print("Actividad:", agenda[clave])
else:
    print("No hay actividad agendada.")

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