'''Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience
leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar 
el precio habitual de una barra de pan,
el descuento que se le hace por no ser fresca y el coste final total.'''

barras_de_ayer= int(input("¿Cuántas barras no son del día?: "))
coste_barra_del_dia = 3.49
descuento_por_no_ser_del_dia = "60%"
descuento = 0.6

precio_total = (coste_barra_del_dia - (coste_barra_del_dia * descuento) ) * barras_de_ayer
print(f'Cada barra cuesta {coste_barra_del_dia}. Si la barra no es de hoy, tiene un descuento de {descuento_por_no_ser_del_dia}. El precio total de tus barras es: {precio_total}')


