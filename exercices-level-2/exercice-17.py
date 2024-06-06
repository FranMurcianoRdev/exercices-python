'''Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla 
el capital obtenido en la inversión.'''

print('Cantidad de dinero a invertir: ')
cantidad_dinero = float(input())
print('Interés anual: ')
interes= float(input())
print('Número de años: ')
años= float(input())
capital_obtenido = interes * años * cantidad_dinero
print(f"El capital obtenido con la inversión es: {capital_obtenido}")