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

