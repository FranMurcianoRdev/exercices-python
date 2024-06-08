'''Escribir un programa que pregunte por consola el precio de un
producto en euros con dos decimales y muestre por pantalla el número de euros y 
el número de céntimos del precio introducido.'''

#Pedir al usuario que introduzca el precio
precio = str(input('Introduzca el precio: '))

#Obtener los euros y los centimos
euros = precio.split(".")[0]
centimos= precio.split(".")[1]

#Mostrar en la consola el resultado

print(f'El precio del producto son {euros} euros con {centimos} céntimos')

