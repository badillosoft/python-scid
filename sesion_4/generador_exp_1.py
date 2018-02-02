import random

f = open("experimento.csv", "w")

for t in range(0, 181, 5):
    T = random.uniform(60, 100)
    PH = random.uniform(-7, 7)
    M = random.uniform(10. / 60, 10. / 100)
    print("{} {} {} {}".format(t, T, PH, M))
    f.write("{},{},{},{}\n".format(t, T, PH, M))

f.close()