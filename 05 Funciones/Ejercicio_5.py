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