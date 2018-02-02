f = open("datos.csv", "r")

keys = f.readline().split(",")

for linea in f:
    values = linea.split(",")
    p = {}
    for i in range(0, len(keys)):
        k = keys[i]
        v = values[i]
        p[k] = v
    print(p)

f.close()