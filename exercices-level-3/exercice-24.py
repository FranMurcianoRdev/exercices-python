'''Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde 
el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el
número de teléfono sin el prefijo y la extensión.'''

telefono = input("Escriba su número de teléfono (prefijo-numero-extension): ")

nuevo_telefono = telefono[4:len(telefono)-3:1]
print(nuevo_telefono)