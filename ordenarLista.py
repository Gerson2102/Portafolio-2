# Función: Ordenar lista, ordena los números de una lista de forma ascendente
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