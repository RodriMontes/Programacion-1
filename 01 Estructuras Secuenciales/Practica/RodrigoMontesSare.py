# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print('Hola Mundo!')

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla. 

nombre = input('Hola, ingresa tu nombre: ')
print(f'Hola {nombre}')

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla. 

nombre = input('Hola, ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')
edad = input('Ingresa tu edad: ')
residencia = input('Ingresa tu lugar de residencia: ')

print(f'Soy {nombre} {apellido}, tengo {edad} anos y vivo en {residencia}')

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 

radio = int(input('Escribe el radio del circulo'))
area = 3.14 * (radio ** 2)
perimetro = 2 * radio * 3.14

print(f'El area del circulo es: {area} y el perimetro es: {perimetro}')

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale.  cantidad_horas = round(cantidad_segundos / 3600, 2) para que tenga dos decimales tambien se puede usar

segundos = int(input('Ingrese la cantidad de segundos:'))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.  No se uso bucles ya que no se vio en esta activdad 

numero = int(input("Ingrese un número: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

a = int(input("Ingrese el primer número entero distinto de 0: "))
b = int(input("Ingrese el segundo número entero distinto de 0: "))

suma = a + b
division = a / b
multiplicacion = a * b
resta = a - b

print(f"Suma: {suma}")
print(f"División: {division:.2f}")
print(f"Multiplicación: {multiplicacion}")
print(f"Resta: {resta}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
# modo:  

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc:.2f}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 

temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = (9/5) * temp_celsius + 32
print(f"La temperatura en Fahrenheit es: {temp_fahrenheit:.2f}")

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números. 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio:.2f}")