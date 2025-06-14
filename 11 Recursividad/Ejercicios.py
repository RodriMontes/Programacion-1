## 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
    print(f"El factorial de {i} es {factorial(i)}")


## 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

pos = int(input("Ingrese la posición para la serie de Fibonacci: "))
for i in range(pos + 1):
    print(f"F({i}) = {fibonacci(i)}")

## 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Ejemplo de uso:
base = int(input("Base: "))
exp = int(input("Exponente: "))
print(f"{base}^{exp} = {potencia(base, exp)}")

## 4

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# Ejemplo de uso:
numero = int(input("Número en decimal: "))
binario = decimal_a_binario(numero)
print(f"Binario: {binario if binario else '0'}")

## 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejemplo de uso:
texto = input("Ingrese una palabra: ").lower()
print("Es palíndromo:", es_palindromo(texto))

## 6

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# Ejemplo de uso:
num = int(input("Número: "))
print(f"Suma de dígitos: {suma_digitos(num)}")

## 7

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Ejemplo de uso:
bloques = int(input("Bloques en el nivel inferior: "))
print(f"Total de bloques: {contar_bloques(bloques)}")

## 8 
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    contador = 1 if numero % 10 == digito else 0
    return contador + contar_digito(numero // 10, digito)

# Ejemplo de uso:
n = int(input("Número: "))
d = int(input("Dígito a contar (0-9): "))
print(f"El dígito {d} aparece {contar_digito(n, d)} veces.")