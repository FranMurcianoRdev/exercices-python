'''Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
y después muestre por pantalla
la misma frase pero con la vocal introducida en mayúscula'''

# Pedir al usuario que introduzca una frase
frase = input("Introduce una frase: ")

# Pedir al usuario que introduzca una vocal
vocal = input("Introduce una vocal: ")

# Convertir la vocal a mayúscula
vocal_mayuscula = vocal.upper()

# Reemplazar todas las ocurrencias de la vocal para la vocal en mayuscula
frase_modificada = frase.replace(vocal, vocal_mayuscula)

# Mostrar la frase modificada por pantalla
print(frase_modificada)
