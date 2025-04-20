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
