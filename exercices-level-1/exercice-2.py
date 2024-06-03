'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. '''

def custom_max(n1: int, n2: int, n3: int): 
    
    """Función que retorna el valor más grande comparando tres números

    Args:
        n1 (int): Primer número a comparar
        n2 (int): Segundo número de la comparación
        n3 (int): Tercer número de la comparación

    Returns:
        int: Mayor número de los dos argumentos

    n1 > n2 > n3 # return n1
    n2 > n3 # n1 no es mayor que n2, entonces return n3 si se cumple esta condición
    n3 # si no se cumple ninguna de las otras condiciones, n3 es el mayor, return n3
    """

    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3:
        return n2
    else: 
        return n3

print(custom_max(1, 2, 3))
print(custom_max(4, 1, 3))
print(custom_max(6, 7, 1))