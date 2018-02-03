f = open("experimento.csv", "r")

f.readline()

tiempos = []
temperaturas = []
phs = []
mus = []

for linea in f: # "0,60.0,0.0,0.16666666666666666"
    d = linea.split(",") # ["0", "60.0" , "0.0" , "0.16666666666666666"]
    tiempos.append(float(d[0])) # append(0.0)
    temperaturas.append(float(d[1])) # append(60.0)
    phs.append(float(d[2])) # append(0.0)
    mus.append(float(d[3])) # append(0.16666666666666666)

# print("t: {}".format(tiempos)) # [0, 5, 10, 15, 20, ...]
# print("T: {}".format(temperaturas)) # [61..., 62..., 63...]
# print("PH: {}".format(phs))
# print("M: {}".format(mus))

import matplotlib.pyplot as plt

# Recuperamos la figura y la lista de graficas
fig, axes = plt.subplots(nrows=3, ncols=1)

# axes = [g0, g1, g2]

# g0.plot(...)
axes[0].plot(tiempos, temperaturas, "ro")
axes[0].set_title("Temperatura")

# g1.plot(...)
axes[1].plot(tiempos, phs, "bo")
axes[1].set_title("PH")

# g2.plot(...)
axes[2].plot(tiempos, mus, "go")
axes[2].set_title("Mu")

plt.savefig("experimento2.png")

plt.show()