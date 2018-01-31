def ordenar(A):
    B = []

    while len(A) > 0:
        x = min(A)
        A.remove(x)
        B.append(x)

    return B

print(ordenar([1, 2, 5, 3, 2, 0, 9, 5, 4, 6, 7, 3]))