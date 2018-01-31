def Integral(f, a, b, n):
    I = 0
    d = float(b - a) / n
    for i in range(1, n + 1):
        xi_1 = a + (i - 1) * d
        xi = a + i * d
        fi_1 = f(xi_1)
        fi = f(xi)
        Hi = (fi + fi_1) / 2.
        Ai = Hi * d
        I = I + Ai
    return I

def f(x):
    return x ** 2 + 3

def g(x):
    return 2 * x - 4

r1 = Integral(f, 1, 10, 100)

r2 = Integral(g, -10, 10, 40)

r3 = Integral(lambda x: x ** 2 + 3, 1, 10, 100)
r4 = Integral(lambda x: 2 * x - 4, -10, 10, 40)

print("Integral de f(x) = {}".format(r1))
print("Integral de g(x) = {}".format(r2))
print("Integral de ?(x) = {}".format(r3))
print("Integral de ?(x) = {}".format(r4))


print("R1: {} R2: {} R3: {} R4: {}".format(r1, r2, r3, r4))