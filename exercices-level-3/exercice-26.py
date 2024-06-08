'''Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
y después muestre por pantalla
la misma frase pero con la vocal introducida en mayúscula'''


#Pedir al usuario que introduzca una frase 
frase = str(input("Introduzca una frase: "))

#Pedir al usuario que introduzca una vocal
vocal = str.lower((input("Introduzca una vocal para sustituir: ")))

#transformar la vocal en mayúscula 
vocal_mayuscula = vocal.upper()

#Reemplazar todas las vocales seleccionadas que haya en la frase por la nueva vocal en mayúscula
nueva_frase = frase.replace(vocal, vocal_mayuscula)

#Mostrar en pantalla la nueva frase
print(nueva_frase)