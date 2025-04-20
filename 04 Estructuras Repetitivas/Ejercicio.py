# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

while True:
    numUser = input('Ingresa un numero entero:')
    
    try:
        numero = int(numUser)

        if numero == 0:
            cantidadDigitos = 1
        else:
            cantidadDigitos = len(str(abs(numero))) #lo pasamos a valor absoluto y obtenemos su longitud, con abs() ignoramos el signo negativo

        print(f"El número {numero} tiene {cantidadDigitos} dígito(s).")
        break

    except ValueError:
        print("Error: La entrada no es un número entero válido. Inténtelo de nuevo.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 


try:
    #  Solicitar los dos números al usuario 
    num1_str = input("Introduce el primer número entero: ")
    num2_str = input("Introduce el segundo número entero: ")

    # Pasamos los numeros a int
    num1 = int(num1_str)
    num2 = int(num2_str)

    # Determinamos cual es el menor y mayor
    numMin = min(num1, num2)
    numMax = max(num1, num2)

    # Suma 
    sumatotal = 0

    for i in range (numMin+1, numMax):
        sumatotal += i

    if numMax - numMin <= 1:
         # No hay números enteros estrictamente entre ellos (ej: 5 y 6, o 5 y 5)
         print(f"No hay números enteros estrictamente entre {num1} y {num2}. La suma es: 0")
    else:
         # Sí hay números entre ellos
         print(f"La suma de los números enteros entre {num1} y {num2} (excluyendo {num1} y {num2}) es: {sumatotal}")

except ValueError:
    # --- Manejar el caso en que la entrada no es un entero válido
    print("Entrada no válida. Por favor, introduce solo números enteros.")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

sumaTotal = 0

while True:
    numUser = input('Ingresa un numero entero:')
    
    try:
        numero = int(numUser)

        if numero == 0:
            print(f"El total es {sumaTotal}).")
            break
        else:
            sumaTotal += numero

    except ValueError:
        print("Error: La entrada no es un número entero válido. Inténtelo de nuevo.")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

secretNum = random.randint(0,9)
print(secretNum)
intentos = 0

while True:
    numUser = input('Ingresa un numero entero entre 0 a 9:')
    intentos += 1
    try:
        numero = int(numUser)

        if not (0 <= numero <= 9):
            print('Tu numero esta fuera del rango del juego')

        if secretNum == numero:
            print(f'Ganaste! en {intentos} intento/s')
            break

    except ValueError:
        print("Error: La entrada no es un número entero válido. Inténtelo de nuevo.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for numero in range(100, -1, -2):
  print(numero)

print("Fin de la lista.")

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

try:
    #  Solicitar los dos números al usuario 
    num1_str = input("Introduce el primer número entero: ")

    # Pasamos los numeros a int
    num1 = int(num1_str)

    if num1 >= 0:
        sumaTotal = 0
        for i in range(0, num1+1):
            sumaTotal += i

        print(f"La suma de todos los números enteros desde 0 hasta {num1} es: {sumaTotal}")

    else:
        print("Error: Debes introducir un número entero positivo o cero.")

except ValueError:
    # --- Manejar el caso en que la entrada no es un entero válido
    print("Entrada no válida. Por favor, introduce solo números enteros.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 


pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range (0, 101):
    
    try:
        numero = int(input('Ingresa un numero entero: '))

        if numero >= 0:
            positivos += 1
            if numero %2 == 0:
                pares += 1
            else:
                impares += 1
        else:
            negativos += 1
            if numero %2 == 0:
                pares += 1
            else:
                impares += 1

    except ValueError:
        # --- Manejar el caso en que la entrada no es un entero válido
        print("Entrada no válida. Por favor, introduce solo números enteros.")

print(f'La cantidad de numeros pares es: {pares}, impares: {impares}, positivos: {positivos}, negativos: {negativos}')

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).


CANTIDAD_NUMEROS_A_INGRESAR = 5 # <-- Cambia este valor a 100 para el requisito final

suma_total = 0             # Variable para acumular la suma de los números válidos
numeros_validos_contados = 0 # Variable para contar cuántos números enteros válidos se ingresaron

print(f"Por favor, ingresa {CANTIDAD_NUMEROS_A_INGRESAR} números enteros.")


for i in range(CANTIDAD_NUMEROS_A_INGRESAR):
    prompt = f"Ingresa el número #{i + 1}: "

    try:
        numeroStr = input(prompt)
        numeroIngresado = int(numeroStr)
        suma_total = suma_total + numeroIngresado # O de forma corta: suma_total += numero_ingresado
        numeros_validos_contados = numeros_validos_contados + 1 # O de forma corta: numeros_validos_contados += 1

    except ValueError:
        # Si la entrada NO pudo ser convertida a entero (ej: el usuario escribió "abc"):
        print("¡Entrada no válida! Eso no parece un número entero. Este valor será ignorado.")
        # El bucle automáticamente pasará a la siguiente iteración.

print("\n--- Resultado del Cálculo ---") # Separador para mejor presentación

if numeros_validos_contados > 0:
    media = suma_total / numeros_validos_contados
    print(f"Se ingresaron {numeros_validos_contados} números enteros válidos.")
    print(f"La suma total de los números ingresados es: {suma_total}")
    print(f"La media (promedio) de los números ingresados es: {media}")
else:
    # Si no se ingresó ningún número válido, no podemos calcular la media
    print("No se ingresó ningún número entero válido. No se puede calcular la media.")


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
