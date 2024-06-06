'''Definir un histograma procedimiento() que tome una lista de números enteros e imprima un
histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
******* '''

def procedimiento(lista: list):
    """Función que devuelve un histograma dependiendo de la cantidad de números y su valor de una lisrta

    Args:
        lista (list): lista de números para realizar el histograma

    Returns:
        list: Lista con el histograma
    """
    
    histograma = '*'
    result = []
    for i in lista:
        result.append(histograma * i)
    return "\n".join(result) #! join devuelve todos los valores de una lista separados por el valor que se pone delante, en este caso, un salto de linea

lista1 = [2, 4, 6]
lista2 = [6, 6, 6]
lista3 = [12, 41, 61]
print(procedimiento(lista1))
print(procedimiento(lista2))
print(procedimiento(lista3))