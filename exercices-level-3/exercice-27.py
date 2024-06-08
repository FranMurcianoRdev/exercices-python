'''Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.'''

#Pedir el correo electrónico
email = str(input('Introduce el correo electrónico: '))

#Crear nuevo dominio
nuevo_dominio = '@ceu.es'

#Crear nuevo email, seleccionando solo la primera parte del introducido por el usuario.
nuevo_email = email.split('@')[0] + nuevo_dominio

#mostrar en pantalla el nuevo email 
print(nuevo_email)
