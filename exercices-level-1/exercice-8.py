'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1
miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for
anidado. '''

def superposicion(lista1: list, lista2: list):
    """Función que devuelve True or false si los datos de una lista al menos se repiten una vez

    Args:
        lista1 (list): Primera lista a evaluar
        lista2 (list): Segunda lista a evaluar

    Returns:
        boolean: True or false si cualquier valor aparece en las dos listas a la vez
    """
    for i in lista1: 
        for j in lista2: 
            if j == i: 
                return True
    return False

lista1= [1, 2, 3]
lista2= [2, 4, 5]
lista3= ["a", "b", "c"]
lista4= ["d", 5, 3]

print(superposicion(lista1, lista2))
print(superposicion(lista2, lista3))
print(superposicion(lista3, lista4))
print(superposicion(lista4, lista1))