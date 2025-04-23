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