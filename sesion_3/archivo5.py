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

hombres = []
mujeres = []

for p in personas:
    if p["sexo"] == "H":
        hombres.append(p)
    else:
        mujeres.append(p)

print("Hombres: {}".format(hombres))
print("Mujeres: {}".format(mujeres))

TH = len(hombres)
TM = len(mujeres)

T = TH + TM

pH = float(TH) / T * 100
pM = float(TM) / T * 100

print("-" * 80)

print("Total de personas: {}".format(T))
print("Hombres: {} {}%".format(TH, pH))
print("Mujeres: {} {}%".format(TM, pM))

