# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
#  
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más 


def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Ejemplo de uso:
bloques = int(input("Bloques en el nivel inferior: "))
print(f"Total de bloques: {contar_bloques(bloques)}")