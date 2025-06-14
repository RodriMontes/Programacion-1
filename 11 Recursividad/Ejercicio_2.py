# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

pos = int(input("Ingrese la posición para la serie de Fibonacci: "))
for i in range(pos + 1):
    print(f"F({i}) = {fibonacci(i)}")