'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad
de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y
mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
Redondear cada cantidad a dos decimales.'''

cantidad_inicial = float(input("Introduce la cantidad inicial para ahorrar: "))
intereses = 0.04

ahorro_primer_año = round((cantidad_inicial * intereses) + cantidad_inicial,2)
print(f'El dinero ahorrado en el primero año es: {ahorro_primer_año}')
ahorro_segundo_año = round((ahorro_primer_año * intereses) + ahorro_primer_año, 2)
print(f'El dinero ahorrado en el primero año es: {ahorro_segundo_año}')
ahorro_tercer_año = round((ahorro_segundo_año * intereses) + ahorro_segundo_año,2)
print(f'El dinero ahorrado en el primero año es: {ahorro_tercer_año}')