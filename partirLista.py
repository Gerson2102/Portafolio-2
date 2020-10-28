# Función: Partir lista
# Entradas: Un elemento de tipo lista
# Salidas: Una lista con sublistas de solo los números positivos
# Restricciones: Solo entran elementos de tipo lista

def partirLista (lista):
    if isinstance (lista, list) and (lista != []):
        return partirLista_aux (lista, [], [])
    else:
        return "Error, el elemento de entrada debe de ser una lista y no debe de estar vacía"


def partirLista_aux (p_lista, p_sublista, p_resultado):
    if p_lista == []:
        return p_resultado + [p_sublista]
    elif p_lista [0] >= 0:
        return partirLista_aux (p_lista [1:], p_sublista + [p_lista [0]], p_resultado)
    else:
        return partirLista_aux (p_lista [1:], [], p_resultado + [p_sublista])