A = [1, 4, 5, 7, 2, 3, 9, 8, 3, 5, 6]

P = []
I = []

for x in A:
    if x % 2 == 0:
        P.append(x)
    else:
        I.append(x)

print("Pares: {}".format(P))
print("Impares: " + str(I))