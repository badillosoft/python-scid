import math

f = open("experimento.csv", "r")

f.readline()

def F_T(t):
    return ((100 - 60) / (180 - 0)) * (t - 0) + 60

def F_PH(t):
    return 7 * math.sin(3 * math.pi * t / 180)

def F_Mu(T, PH):
    return 10 * T / (T + PH) ** 2

ti = []

T_e = []
PH_e = []
M_e = []

T_r = []
PH_r = []
M_r = []

for linea in f: # "0,60.0,0.0,0.16666666666666666"
    d = linea.split(",") # ["0", "60.0" , "0.0" , "0.16666666666666666"]
    
    t = float(d[0])
    T = float(d[1])
    PH = float(d[2])
    M = float(d[3])

    T_ = F_T(t)
    PH_ = F_PH(t)
    M_ = F_Mu(T_, PH_)
    
    ti.append(t)

    T_e.append(T)
    PH_e.append(PH)
    M_e.append(M)
    
    T_r.append(T_)
    PH_r.append(PH_)
    M_r.append(M_)

def ECM(E, R): # Recibo dos listas E y R
    S = 0 # Sumo el error al cuadrado
    n = min(len(E), len(R)) # obtengo el menor tamanio de las listas
    for i in range(n):
        e = (E[i] - R[i]) ** 2 # calculo el error cuadratico para el punto i
        S = S + e # S += e # acumulo el error en S
    return S / (n - 1) # regreso la suma en n - 1 (varianza)

import matplotlib.pyplot as plt

# Recuperamos la figura y la lista de graficas
fig, axes = plt.subplots(nrows=3, ncols=1)

# axes = [g0, g1, g2]

# g0.plot(...)
axes[0].plot(ti, T_e, "ro")
axes[0].plot(ti, T_r, "c-")
axes[0].set_title("Temperatura")
tex = "ECM: {:.2f}".format(ECM(T_e, T_r))
axes[0].text(125, 70, tex, fontsize=10, va='top')

# g1.plot(...)
axes[1].plot(ti, PH_e, "bo")
axes[1].plot(ti, PH_r, "c-")
axes[1].set_title("PH")
tex = "ECM: {:.2f}".format(ECM(PH_e, PH_r))
axes[1].text(125, -4, tex, fontsize=10, va='top')

# g2.plot(...)
axes[2].plot(ti, M_e, "go")
axes[2].plot(ti, M_r, "c-")
axes[2].set_title("Mu")
tex = "ECM: {:.6f}".format(ECM(M_e, M_r))
axes[2].text(125, 0.15, tex, fontsize=10, va='top')

plt.savefig("experimento2.png")

plt.show()