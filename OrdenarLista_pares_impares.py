def ordenarLista_pares_impares (lista_1, lista_2):
    if isinstance (lista_1, list) and (lista_1 != []) and (lista_2 != []) and isinstance (lista_2, list):
        return ordenarLista_pares_impares_aux (lista_1, lista_2, [], [], [])
    else:
        return "Error, elementos de entrada incorrectos"


def ordenarLista_pares_impares_aux (lista_1, lista_2, pares, impares, resultado):
    if (lista_1 == []) and lista_2 == []:
        return resultado + [ordenarLista (pares, contadorLargoLista (pares), 0, 0)] + [ordenarLista (impares, contadorLargoLista (impares), 0, 0)]
    else:
        if (lista_1 [0] % 2 == 0) and (lista_2 [0] % 2 == 0):
            return ordenarLista_pares_impares_aux (lista_1 [1:], lista_2 [1:], pares + [lista_1 [0]] + [lista_2 [0]], impares, resultado)
        elif (lista_1 [0] % 2 != 0) and (lista_2 [0] % 2 != 0):
            return ordenarLista_pares_impares_aux (lista_1 [1:], lista_2 [1:], pares, impares + [lista_1 [0]] + [lista_2 [0]], resultado)
        elif (lista_1 [0] % 2 != 0) and (lista_2 [0] % 2 == 0):
            return ordenarLista_pares_impares_aux (lista_1 [1:], lista_2 [1:], pares + [lista_2 [0]], impares + [lista_1 [0]], resultado)
        else:
            return ordenarLista_pares_impares_aux (lista_1 [1:], lista_2 [1:], pares + [lista_1 [0]], impares + [lista_2 [0]], resultado)


def ordenarLista (p_contenido_S, p_largo_lista, p_cont_1, p_cont_2):
     if p_cont_2 == p_largo_lista:
          p_cont_1 += 1
          p_cont_2 = 0
     if p_cont_1 == p_largo_lista:
          return p_contenido_S
     if p_contenido_S[p_cont_1] > p_contenido_S[p_cont_2]:
          return ordenarLista (p_contenido_S, p_largo_lista, p_cont_1, p_cont_2 + 1)
     else:
          numero_mayor = p_contenido_S[p_cont_2]
          p_contenido_S[p_cont_2] = p_contenido_S[p_cont_1]
          p_contenido_S[p_cont_1] = numero_mayor
          return ordenarLista (p_contenido_S, p_largo_lista, p_cont_1, p_cont_2 + 1)


def contadorLargoLista(lista):
     if lista == []:
          return 0
     else:
          return contadorLargoLista(lista[1:]) + 1

