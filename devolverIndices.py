# Función: Devolver los indices de los números
# Entradas: Dos listas
# Salidas: Una lista que posee el índice de la posición de los números de la lista 2
# Restricciones: Solo entran elementos de tipo lista y que no estén vacíos

def devolverIndices (lista_1, lista_2):
    if isinstance (lista_1, list) and isinstance (lista_2, list) and (lista_2 != []) and (lista_1 != []):
        return devolverIndices_aux (lista_1, lista_2, 0, [])
    else:
        return "Error, los lementos deben ser listas y no pueden estar vacías"


def devolverIndices_aux (p_lista_1, p_lista_2, contador, resultado):
    if p_lista_2 == []:
        return resultado
    else:
        if p_lista_1 [0] == p_lista_2 [0]:
            return devolverIndices_aux (p_lista_1 [1:], p_lista_2 [1:], contador + 1, resultado + [contador])
        else:
            return devolverIndices_aux (p_lista_1 [1:], p_lista_2, contador + 1, resultado)