# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario, utilizando un bucle y operaciones aritméticas.

try:
    numStr = input("Introduce un número entero: ")
    num = int(numStr)

    # Guardamos si el número original era negativo
    esNegativo = num < 0

    # Trabajamos con el valor absoluto del número para la inversión de dígitos

    numero_restante = abs(num)

    # Inicializar la variable para el número invertido 
    numero_invertido = 0

    #  Bucle para invertir los dígitos aritméticamente 
    # El bucle continúa mientras queden dígitos en numero_restante
    while numero_restante > 0:
        # Obtener el último dígito del número_restante
        # El operador módulo (%) da el resto de la división por 10, que es el último dígito
        ultimo_digito = numero_restante % 10

        # Construir el número invertido:
        # 1. Multiplicar numero_invertido por 10 para mover los dígitos existentes a la izquierda
        # 2. Sumar el ultimo_digito obtenido para añadirlo al final
        numero_invertido = numero_invertido * 10 + ultimo_digito

        # Eliminar el último dígito de numero_restante
        # La división entera (//) por 10 remueve el último dígito
        numero_restante = numero_restante // 10

    if esNegativo:
        numero_invertido = -numero_invertido

    #  Mostrar el resultado 
    print(f"El número original es: {num}")
    print(f"El número con los dígitos invertidos es: {numero_invertido}")

except ValueError:
    print("Entrada no válida. Por favor, introduce solo un número entero válido.")
