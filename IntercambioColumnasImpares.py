def largo (lista, cont):
    if lista == []:
        return cont
    else:
        return largo (lista [1:], cont + 1)


def intercambio_columnas_impares (m):
    largoC = largo (m[0], 0)
    largoF = largo (m, 0)

    return intercambio_columnas (m, largoF, largoC, 0, 1, ((largoF + 1) // 2))


def intercambio_columnas_impares_aux (m, f, c, c1, c2, mitad):
    if (c2 > c):
        return m
    else:
        tempo = m [c1][c2]
        m[c1][2] = m[mitad][c2]
        m[mitad][c2] = tempo
        return intercambio_columnas_impares_aux (m, f, c, c1, c2 + 2, mitad)


def intercambio_columnas (m, f, c, c1, c2, mitad):
    if (c1 >= ((f + 1) // 2)):
        return m
    else:
        intercambio_columnas_impares_aux (m, f, c, c1, c2, mitad)
        return intercambio_columnas (m, f, c, c1 + 1, 1, mitad + 1)

