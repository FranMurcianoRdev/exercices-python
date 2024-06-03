'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.'''

def len_custom(cadena):
    """Función que retorna la longitud de una lista o cadena de caracteres

    Args:
        cadena (list or string): Cadena para calcular su longitud

    Returns:
        int: longitud de la cadena
    """
    number = 0
    for i in cadena: 
        number +=1
    return number

print(len_custom("prueba"))
print(len_custom([1, 2, 3, 4, 5, 6]))