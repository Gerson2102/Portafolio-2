# Función: Partir lista con variación de que si las sublista está vacía se omita
def partirLista(lista):
    if isinstance (lista, list) and (lista != []):
        return partirListaAux (lista, [], [], [])
    else:
        return "Error"


def partirListaAux (p_lista, p_sublista, p_lista_negativos, p_resultado):
    if p_lista == []:
        if p_sublista == []:
            return p_resultado + [p_lista_negativos]
        else:
            return p_resultado + [p_sublista] + [p_lista_negativos]
    elif p_lista [0] >= 0:
        return partirListaAux (p_lista [1:], p_sublista + [p_lista [0]], p_lista_negativos, p_resultado)
    else:
        return partirListaAux (p_lista [1:], [], p_lista_negativos + [p_lista [0]], p_resultado + [p_sublista])