f = open("datos.csv", "r")

cabeceras = f.readline()

for linea in f:
    d = linea.split(",")
    p = {
        "nombre": d[0],
        "edad": int(d[1]),
        "sexo": d[2],
        "salario": float(d[3])
    }
    print(p)

f.close()