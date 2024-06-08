'''Escribir un programa que pregunte al usuario la fecha de su 
nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
Adaptar el programa anterior para que también funcione cuando
el día o el mes se introduzcan con un solo carácter.'''

from datetime import datetime

#Pedirle al usuario que introduzca la fecha de su nacimiento
fecha = input('Introduzca la fecha de su nacimiento (dd/mm/yy):')

#transformar la fecha en un objeto datetime
fecha = datetime.strptime(fecha, "%d/%m/%Y")

#Obtener los resultados

dia = fecha.day
mes = fecha.month
año = fecha.year

print(dia)
print(mes)
print(año)