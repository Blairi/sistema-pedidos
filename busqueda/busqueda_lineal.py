
def busqueda_lineal(A, attr, key):

    for i in range( len(A) ):
        if key == attr(A[i]):
            return i

    return -1