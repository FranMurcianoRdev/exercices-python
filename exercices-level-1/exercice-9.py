'''Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter
multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".'''

def generar_n_caracteres(n: int, caracter: str):
    """Función que devuelve un caracter multiplicado n veces

    Args:
        n (int): Valor para multiplicar un caracter 'x' veces
        caracter (str): Caracter que aparecerá duplicado tantas veces como n se haya indicado

    Returns:
        str: resultado de multiplicar un caracter, n veces
    """
    return n*caracter

print(generar_n_caracteres(2, "a"))
print(generar_n_caracteres(2, "0"))
print(generar_n_caracteres(3, "oooowwww"))