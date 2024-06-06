'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos 
en el último pedido y calcule el peso total del paquete que será enviado.'''

peso_payaso = 112
peso_muñeca = 75

def peso_total(num_muñecas: int, num_payasos: int):
    peso_total = (num_muñecas * peso_muñeca) + (num_payasos * peso_payaso)
    return peso_total

print('¿Cuántas muñecas se han vendido?')
num_muñecas = int(input())
print('¿Cuántos payasos se han vendido?')
num_payasos = int(input())

print(peso_total(num_muñecas, num_payasos))