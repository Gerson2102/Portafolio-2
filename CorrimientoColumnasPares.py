def corrimiento1_columnas_pares(matriz):
    if isinstance(matriz,list):
        if largo(matriz, 0) == largo(matriz[0], 0):
            return corrimiento1_columnas_pares_aux(matriz,0,0)
        else:
            return "Error, no cumple las condiciones de matriz"
    else:
        return "Error, parámetro de entrada incorrecto"


def corrimiento1_columnas_pares_aux(matriz,i,j):
    if i == (largo(matriz, 0)-1):
        return matriz
    if j == largo(matriz, 0):
        return corrimiento1_columnas_pares_aux(matriz,i+1,0)
    if j % 2 == 0:
        temp=matriz[-i+1][j]
        matriz[-i+1][j]=matriz[-i][j]
        matriz[-i][j]=temp
        return corrimiento1_columnas_pares_aux(matriz,i,j+2)
    else:
        return corrimiento1_columnas_pares_aux(matriz,i,j+1)


def largo (lista, cont):
    if lista == []:
        return cont
    else:
        return largo (lista [1:], cont + 1)        