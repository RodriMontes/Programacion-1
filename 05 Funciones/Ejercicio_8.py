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