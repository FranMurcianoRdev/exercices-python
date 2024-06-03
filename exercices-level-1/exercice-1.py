'''Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un
muy buen ejercicio'''

def custom_max(n1: int, n2: int): #! La función no puede llamarse 'max()' porque ya existe en python
    """Función que retorna el valor más grande comparando dos números

    Args:
        n1 (int): Primer número a comparar
        n2 (int): Segundo número de la comparación

    Returns:
        int: Mayor número de los dos argumentos
    """

    if n1>n2: 
        return n1
    else: 
        return n2
    

print(custom_max(2, 3))
print(custom_max(3, 3))
print(custom_max(3, 1))