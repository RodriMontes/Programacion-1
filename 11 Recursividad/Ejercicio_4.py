# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# Ejemplo de uso:
numero = int(input("Número en decimal: "))
binario = decimal_a_binario(numero)
print(f"Binario: {binario if binario else '0'}")