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