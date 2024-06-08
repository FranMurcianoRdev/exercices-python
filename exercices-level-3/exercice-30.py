'''Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
separados por comas, y muestre por pantalla
cada uno de los productos en una línea distinta.'''

#Pedir la lista de la compra
lista_compra = str(input("Introduce la lista de la compra: "))

# Separar los productos por comas
productos = lista_compra.split(',')

# Imprimir cada producto en una línea distinta
for producto in productos:
    print(producto.strip()) #strip() elimina espacios en blanco