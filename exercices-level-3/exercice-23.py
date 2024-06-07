'''Escribir un programa que pregunte el nombre del usuario en la consola y
después de que el usuario lo introduzca muestre por 
pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número 
de letras que tienen el nombre.'''

nombre = str(input('Introduzca el nombre de usuario: '))

n = 0
for i in nombre: 
    if i == " ": #Por si quisieramos no contar los espacios como una letra
        n -= 1
    n += 1

print((nombre).upper() + f" tiene {n} letras")
