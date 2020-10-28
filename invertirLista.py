def invertirLista (lista):
    if isinstance (lista, list) and (lista != []):
        return invertirLista_aux (lista, [])
    else:
        return "Error, el elemento de entrada debe ser una lista y no debe de estar vacía"


def invertirLista_aux (p_lista, p_resultado):
    if p_lista == []:
        return p_resultado
    else:
        if (p_lista [-1], int) and (p_lista [-1] >= 0):
            return invertirLista_aux (p_lista [:-1], p_resultado + [p_lista [-1]])
        else:
            return invertirLista_aux (p_lista [:-1], p_resultado)