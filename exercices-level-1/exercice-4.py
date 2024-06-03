'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''

def is_vocal(caracter: str):
    """Función que debe comprobar si un caracter es una vocal o no

    Args:
        caracter (str): caracter a evaluar si es vocal o no

    Returns:
        boolean: True si es vocal o false si no lo es
    """

    vocales = ["a", 'e', 'i', 'o', 'u']

    if caracter in vocales: 
        return True
    else: 
        return False
    

print(is_vocal("a"))
print(is_vocal("b"))
print(is_vocal("o"))