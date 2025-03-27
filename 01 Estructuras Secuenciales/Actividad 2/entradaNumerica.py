# Usamos la funcion input para pedir un numero entero al usuario
numeroEntero = input('Por favor, escribe un numero entero:')

# Convertimos (casteamos) el dato ingresado a un numero intero con int()
numeroEntero = int(numeroEntero)

# Mostramos el numero entero usando print
print('El numero entero que ingresaste es:', numeroEntero)

# Pedimos al usuario un numero decimal
numeroDecimal = input('Ahora ingresa un numero decimal:')

# Convertimos el dato a un float
numeroDecimal = float(numeroDecimal)

#Mostramos el valor 
print('El numero decimal es',numeroDecimal)

#Ejemplo: Operamos con los numeros ingresados
suma = numeroEntero + numeroDecimal
print('La suma es: ', suma)
