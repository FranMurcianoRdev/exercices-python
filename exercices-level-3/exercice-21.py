'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como 
el número introducido.'''

nombre = str(input("Introduce tu nombre de usuario: "))
numero = int(input("Introduce cuántas veces quieres que se repita tu nombre: "))

for i in range(numero):
    print(nombre)