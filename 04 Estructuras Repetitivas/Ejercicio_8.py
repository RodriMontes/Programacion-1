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