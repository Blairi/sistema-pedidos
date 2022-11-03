
def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


def partition(A, attr, l, h):
    i = l - 1
    pivot = A[h]
    j = l
    while j < h:
        if attr(A[j]) <= attr(pivot):
            i = i + 1
            swap( A, i, j )

        j = j + 1
    swap( A, i + 1, h )
    return i + 1


def quick_sort(A, attr, l, h):
    if l < h:
        pi = partition( A, attr, l, h )
        quick_sort( A, attr, l, pi - 1 )
        quick_sort( A, attr, pi + 1, h )
