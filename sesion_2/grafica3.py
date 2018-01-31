import matplotlib.pyplot as plt

def f(x):
    return x ** 2 - 3

X = []
Y = []

for i in range(0, 100):
    x = i / 10.0
    y = f(x)

    X.append(x)
    Y.append(y)

plt.plot(X, Y, "r-")

plt.show()