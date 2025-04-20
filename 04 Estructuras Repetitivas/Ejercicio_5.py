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
