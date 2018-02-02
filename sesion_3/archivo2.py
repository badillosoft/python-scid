f = open("datos.csv", "r")

cabeceras = f.readline()

for linea in f:
    d = linea.split(",")
    print(d)

f.close()