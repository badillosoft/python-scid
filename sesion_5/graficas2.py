f = open("experimento.csv", "r")

f.readline()

experimentos = []

for linea in f:
    d = linea.split(",")
    e = {
        "t": float(d[0]),
        "T": float(d[1]),
        "PH": float(d[2]),
        "M": float(d[3])
    }
    experimentos.append(e)

print("Experimentos: {}".format(experimentos))

tiempos = list(map(lambda e: e["t"], experimentos))
temperaturas = list(map(lambda e: e["T"], experimentos))
phs = list(map(lambda e: e["PH"], experimentos))
mus = list(map(lambda e: e["M"], experimentos))
