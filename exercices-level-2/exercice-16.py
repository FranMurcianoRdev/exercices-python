'''Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
entera respectivamente. '''

print('Introduzca dos números enteros: ')
n = int(input("1: "))
m = int(input("2: "))
division = n/m
resto = n%m
print(f'El número {n} dividido entre {m}, tiene un cociente de {division} y un resto de {resto}')