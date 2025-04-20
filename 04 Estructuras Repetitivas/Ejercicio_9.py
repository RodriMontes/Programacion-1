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

print("Fin del programa.")