#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 

stock = {
    "arroz": 10,
    "leche": 5,
    "pan": 20
}

producto = input("Ingresá el nombre del producto: ")

if producto in stock:
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto nuevo. Ingresá stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)