f = open("datos.csv", "r")

cabeceras = f.readline()

personas = []

for linea in f:
    d = linea.split(",")
    p = {
        "nombre": d[0],
        "edad": int(d[1]),
        "sexo": d[2],
        "salario": float(d[3])
    }
    personas.append(p)

print(personas)

f.close()