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