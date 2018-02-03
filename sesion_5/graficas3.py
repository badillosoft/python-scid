f = open("experimento.csv", "r")

f.readline()

tiempos = []
temperaturas = []
phs = []
mus = []

for linea in f:
    d = linea.split(",")
    tiempos.append(float(d[0]))
    temperaturas.append(float(d[1]))
    phs.append(float(d[2]))
    mus.append(float(d[3]))

print("t: {}".format(tiempos))
print("T: {}".format(temperaturas))
print("PH: {}".format(phs))
print("M: {}".format(mus))

import matplotlib.pyplot as plt

plt.plot(tiempos, temperaturas, "r-")
plt.plot(tiempos, phs, "b-")
plt.plot(tiempos, mus, "g-")

plt.savefig("experimento.png")