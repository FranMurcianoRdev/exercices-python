'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.'''

print('¿Cuántas horas has trabajado?')
horas_trabajadas = int(input())
print('¿Cuánto cobras por hora?')
coste_hora = int(input())
pago = horas_trabajadas * coste_hora
print(f'Tu paga es: {pago}')