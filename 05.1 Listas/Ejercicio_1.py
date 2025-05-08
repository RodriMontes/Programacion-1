# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
# range.

# Crear una lista con los números del 1 al 100
numero = list(range(1, 101))

# Filtrar los números que sean múltiplos de 4
multiplos_de_4 = [numero for numero in range(1, 101) if numero % 4 == 0]

# Imprimir la lista de números múltiplos de 4
print(multiplos_de_4)
