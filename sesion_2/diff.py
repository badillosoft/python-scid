def Diff(f, x, d):
    return (f(x + d) - f(x)) / d

def h(x):
    return x ** 2 - 3

r1 = Diff(h, 0, 1E-9)
r2 = Diff(h, 1, 1E-4)
r3 = Diff(h, 2.5, 0.0001)

print("h'(0) = {}".format(r1))
print("h'(1) = {}".format(r2))
print("h'(2.5) = {}".format(r3))
