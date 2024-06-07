'''Escribir un programa que pregunte por consola el precio de un
producto en euros con dos decimales y muestre por pantalla el número de euros y 
el número de céntimos del precio introducido.'''

precio = str(input("Introduzca el precio del producto: "))
euros = precio.split(".")[0]
centimos = precio.split(".")[1]

print(f'El precio del producto es: {euros} euros con {centimos} céntimos')