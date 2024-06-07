'''Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.'''

# Pedir al usuario que introduzca su correo electrónico
email = input("Introduzca su correo electrónico: ")

# Separar el nombre del usuario y el dominio antiguo, nos quedamos con la primera parte solo ([0])
nombre_usuario = email.split('@')[0]

# Crear el nuevo correo electrónico con el dominio "ceu.es"
nuevo_correo = nombre_usuario + "@ceu.es"

# Mostrar el nuevo correo electrónico por pantalla
print(nuevo_correo)
