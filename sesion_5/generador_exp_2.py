import random
import math

f = open("experimento.csv", "w")

f.write("t,T,PH,M\n")

def F_T(t):
    return ((100 - 60) / (180 - 0)) * (t - 0) + 60

def F_PH(t):
    return 7 * math.sin(3 * math.pi * t / 180)

def F_Mu(T, PH):
    return 10 * T / (T + PH) ** 2

for t in range(0, 181, 5):
    T = F_T(t)
    PH = F_PH(t)
    M = F_Mu(T, PH)
    print("{} {} {} {}".format(t, T, PH, M))
    f.write("{},{},{},{}\n".format(t, T, PH, M))

f.close()