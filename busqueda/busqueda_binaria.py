
def busqueda_binaria(A, key, attr, inicio, final):

    if inicio > final:
        return False

    m = (inicio + final) // 2

    if attr(A[m]) == key:
        return m

    if attr(A[m]) > key:
        return busqueda_binaria(A, key, attr, inicio, m - 1)

    else:
        return busqueda_binaria(A, key, attr, m + 1, final)
