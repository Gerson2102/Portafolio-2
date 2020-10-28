#Función Devolver Indices V2
def largoLista(lista):
    if isinstance(lista,list):
        return largoLista_aux (lista,0)
    else:
        print("Error en parámetros de entrada")


def largoLista_aux(lista, cont):
    if lista == []:
        return cont
    else:
        return largoLista_aux(lista[1:],cont+1)


def devolverIndicesV2(lista, buscar):
    largo = largoLista(lista)
    if isinstance(lista,list) and isinstance(buscar,list):
        return devolverIndicesV2Aux(lista,buscar,[])
    else:
        print("Error en parámetros de entrada")


def existeValorAux(lista, valor, indice, res):
    if lista == []:
        return res
    elif (lista[0] == valor):
        return existeValorAux(lista[1:], valor, indice + 1, res + [indice])
    else:
        return existeValorAux(lista[1:], valor, indice + 1, res)


def devolverIndicesV2Aux(lista, buscar, res):
    if buscar == []:
        return res
    else:
        lista_temp = existeValorAux(lista, buscar[0], 0, [])
        return devolverIndicesV2Aux(lista, buscar[1:], res + lista_temp)