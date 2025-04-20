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
