# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola():
    print("Hola Mundo")

imprimir_hola()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saluda_usuario(nombre):
    return print(f'Hola {nombre}')

saluda_usuario("Marcos")

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores
# ingresados

def informacion_persona(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

informacion_persona('Rodrigo', 'Montes', 29, 'Argentina')

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

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.


def segundos_a_horas(segundos):
    return segundos/3600

try:
    segundos_usuario = int(input("Ingrese el radio del circulo: "))
    horas = segundos_a_horas(segundos_usuario)


    if isinstance(horas, (int, float)):
        print(f"Los {segundos_usuario} segundos son equivalentes a: {horas:.4f}hs")
    else:
        print(horas)
except ValueError:
  print("Entrada inválida. Por favor, introduce un número para el radio.")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range (0,11):
        print(f"{numero} * {i} = {numero*i}")

try:
    numero_usuario = int(input("Ingrese el numero: "))

    if isinstance(numero_usuario, (int)):
        tabla_multiplicar(numero_usuario)
    else:
        print(numero_usuario)
except ValueError:
  print("Entrada inválida. Por favor, introduce un número para el radio.")

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de 
# sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara


def operaciones_basicas(a, b):

    suma = a + b
    resta = a - b
    multiplicacion = a * b

    #Division por cero
    if b == 0:
        division = None
    else:
        division = a / b
        
    return (suma, resta, multiplicacion, division)

num1 = 10
num2 = 5

resultados = operaciones_basicas(num1, num2)

# Desempaquetar la tupla para acceder a los resultados individuales
sum_res, rest_res, mult_res, div_res = resultados

print(f"Resultados para {num1} y {num2}:")
print(f"  Suma:           {sum_res}")
print(f"  Resta:          {rest_res}")
print(f"  Multiplicación: {mult_res}")

# Verificar si la división fue posible antes de mostrarla
if div_res is not None:
  print(f"  División:       {div_res}")
else:
  print(f"  División:       No se puede dividir por cero.")

print("-" * 20) # Separador para el siguiente ejemplo

# --- Ejemplo con división por cero ---
num3 = 8
num4 = 0

resultados_cero = operaciones_basicas(num3, num4)
sum_cero, rest_cero, mult_cero, div_cero = resultados_cero

print(f"Resultados para {num3} y {num4}:")
print(f"  Suma:           {sum_cero}")
print(f"  Resta:          {rest_cero}")
print(f"  Multiplicación: {mult_cero}")

# Verificar si la división fue posible
if div_cero is not None:
  print(f"  División:       {div_cero}")
else:
  print(f"  División:       No se puede dividir por cero.")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

try:
    peso_usuario = int(input("Ingrese su peso: "))
    altura_usuario = float(input("Ingrese su altura: "))

    if isinstance(peso_usuario, (int)) and isinstance(altura_usuario, float):
        print(f"Su IMC es: {calcular_imc(peso_usuario, altura_usuario)}")

except ValueError:
  print("Entrada inválida. Por favor, introduce un número para el radio.")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):

  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# --- Solicitar la temperatura al usuario y mostrar el resultado ---

try:
  temp_celsius = float(input("Introduce la temperatura en grados Celsius: "))

  # Llamar a la función para convertir a Fahrenheit
  temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

  # Mostrar el resultado de forma clara
  print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F")

except ValueError:
  # Manejar el error si la entrada no es un número
  print("Entrada inválida. Por favor, introduce un valor numérico para la temperatura.")

def calcular_promedio(a, b, c):
  # Sumamos los tres números y dividimos por 3
  promedio = (a + b + c) / 3
  return promedio

try:
  # Pedir los tres números al usuario
  num1 = float(input("Introduce el primer número: "))
  num2 = float(input("Introduce el segundo número: "))
  num3 = float(input("Introduce el tercer número: "))

  # Llamar a la función para calcular el promedio
  promedio_resultado = calcular_promedio(num1, num2, num3)

  # Mostrar el resultado de forma clara23
  print(f"El promedio de {num1}, {num2} y {num3} es: {promedio_resultado:.2f}")

except ValueError:
  # Manejar el error si alguna de las entradas no es un número
  print("Entrada inválida. Por favor, introduce solo valores numéricos.")