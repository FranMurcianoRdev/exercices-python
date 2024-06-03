'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
"estoy probando" debería devolver la cadena "odnaborp yotse"'''

def inversa(cadena: str): 
    """Función que tiene que retornar la cadena pasada como argumento de forma invertida

    Args:
        cadena (str): Cadena a invertir

    Returns:
        str: cadena invertida
    """
    return cadena[::-1]

print(inversa("hola"))
print(inversa("caracola"))
print(inversa("estoy probando"))
print(inversa("estoy probando aún más"))