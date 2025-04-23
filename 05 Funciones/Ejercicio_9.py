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