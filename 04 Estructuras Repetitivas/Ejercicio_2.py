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
