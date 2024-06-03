'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''

def sum_custom(numeros: list):
    """Función que suma los números contenidos en una lista

    Args:
        numeros (list): Lista de numeros a sumar

    Returns:
        int: Suma de todos los números de la lista
    """
    suma = 0 
    
    for i in numeros:
        suma += i 
    return suma

print(sum_custom([1, 2, 3, 4, 5]))
print(sum_custom([1, 1, 1, 1, 1]))
print(sum_custom([100, 1, 1, 1, 1]))

def multiplicar_custom(numeros: list):
    """Función que multiplica los números contenidos en una lista

    Args:
        numeros (list): Lista de numeros a multiplicar

    Returns:
        int: múltiplo de todos los números de la lista
    """
    resultado = 1 # No puede ser '0' porque entonces el resultado siempre daría 0. 
    
    for i in numeros:
        resultado *= i 
    return resultado

print(multiplicar_custom([100, 1, 1, 1, 1]))
print(multiplicar_custom([100, 2, 1, 1, 1]))
print(multiplicar_custom([2, 4, 5, 1, 2]))
