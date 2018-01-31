def ordenar(A):
    n = len(A)
    for i in range(1, n):
        for j in range(0, i):
            if A[i] < A[j]:
                t = A[i]
                A[i] = A[j]
                A[j] = t

X = [4, 3, 1, 4, 2, 3, 4, 3, 7, 8, 5, 6]

ordenar(X)

print(X)