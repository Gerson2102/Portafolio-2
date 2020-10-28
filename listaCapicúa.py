def listaCapicua (lista):
    if isinstance (lista, list):
        if (lista != []):
            return listaCapicua_aux (lista, 0, 0)
        else:
            return False
    else:
        return "Error, el elemento de entrada debe ser una lista y no debe de estar vacía"


def listaCapicua_aux (p_lista, contador, p_resultado):
    if p_lista == []:
        return palindromo (p_resultado)
    else:
        if (p_lista [0], int) and (p_lista [0] >= 0):
            return listaCapicua_aux (p_lista [1:], contador + 1, (p_resultado * 10) + p_lista [0]) 
        else:
            return listaCapicua_aux (p_lista [1:], contador, p_resultado)


def palindromo (num):
    if isinstance (num, int) and (num >= 0):
        resultado = palindromo_aux (num) 
        print (resultado)
    else:
        print("Error") 


def calcular_largo_numero (numero):
    if numero < 10:
        return 1
    else:
        return calcular_largo_numero (numero // 10) + 1


def invertir_numero (num):
    if isinstance (num, int) and (num >= 0):
        resultado = invertir_numero_aux (num, 0)
        return resultado
    else:
        return ("Error") 


def invertir_numero_aux (numero, nuevo_numero):
    if numero < 10:
        return (nuevo_numero * 10) + numero
    else:
        return invertir_numero_aux (numero // 10, (nuevo_numero * 10) + numero % 10) 


def palindromo_aux (num):
    largo_numero = calcular_largo_numero (num)
    mitad_numero_derecho = num % 10**(largo_numero // 2)   
    mitad_numero_derecho_invertido = invertir_numero (mitad_numero_derecho)
    if largo_numero % 2 == 0:
        numero_parte_izquierda = num // 10**(largo_numero // 2)
    else:
        numero_parte_izquierda = num // 10**(largo_numero // 2 + 1)

    if numero_parte_izquierda == mitad_numero_derecho_invertido:
        return (numero_parte_izquierda * 10 ** (calcular_largo_numero (mitad_numero_derecho_invertido))) + (invertir_numero (mitad_numero_derecho_invertido))
    else:
        return False


#print (listaCapicua ([5, 8, 8, 5]))
