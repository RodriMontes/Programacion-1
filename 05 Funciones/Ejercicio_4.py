# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
# y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y 
# devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

import math #para usar math.pi

def calcular_area_circulo(radio):
    if radio < 0:
        return "El radio no puede ser negatvi"
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    if radio < 0:
        return "El radio no puede ser negativo"
    return 2 * math.pi * radio

try:
    radio_usuario = float(input("Ingrese el radio del circulo: "))
    area = calcular_area_circulo(radio_usuario)
    perimetro = calcular_perimetro_circulo(radio_usuario)

    if isinstance(area, (int, float)) and isinstance(perimetro, (int, float)):
        print(f"El area del circulo con radio {radio_usuario} es: {area:.2f}")
        print(f"El permitro del circulo con radio {radio_usuario} es: {perimetro:.2f}")
    else:
        print(area)
except ValueError:
  print("Entrada inválida. Por favor, introduce un número para el radio.")