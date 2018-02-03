import random
import math

f = open("experimento.csv", "w")

f.write("t,T,PH,M\n")

def G_T(t):
    t = t + random.uniform(-10, 10)
    return ((100 - 60) / (180 - 0)) * (t - 0) + 60 + random.uniform(-5, 5)

def G_PH(t):
    return 7 * math.sin(3 * math.pi * t / 180) + random.uniform(-1.5, 1.5)

def G_Mu(T, PH):
    return 10 * T / (T + PH) ** 2 + random.uniform(-0.01, 0.01)

for t in range(0, 181, 5):
    T = G_T(t)
    PH = G_PH(t)
    M = G_Mu(T, PH)
    print("{} {} {} {}".format(t, T, PH, M))
    f.write("{},{},{},{}\n".format(t, T, PH, M))

f.close()