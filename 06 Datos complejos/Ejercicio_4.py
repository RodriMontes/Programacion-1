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
    