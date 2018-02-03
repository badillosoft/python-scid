f = open("experimento.csv", "r")

f.readline()

mat = []

for linea in f:
    d = linea.split(",")
    v = list(map(lambda s: float(s), d)) # [0.0, 60.0, ...]
    mat.append(v)

print(mat)