'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''

def es_palindromo(palabra:str):
    """Función que comprueba si una palabra es o no es palíndroma (se lee de la misma forma del derecho que del revés)

    Args:
        palabra (str): Palabra a evaluar 

    Returns:
        boolean: True or false dependiendo de si es o no palindromo
    """

    nueva_palabra = palabra[::-1]
    if palabra == nueva_palabra:
        return True
    else: 
        return False
    
print(es_palindromo("hola"))
print(es_palindromo("radar"))
print(es_palindromo("estonoespalindromo"))
print(es_palindromo("ana"))