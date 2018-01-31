def f(x):
    return x ** 2 + 3

a = 1.
b = 10.

n = 10000

d = (b - a) / n

I = 0

for i in range(1, n + 1):
    xi_1 = a + (i - 1) * d
    xi = a + i * d
    
    fi_1 = f(xi_1)
    fi = f(xi)

    Hi = (fi + fi_1) / 2

    Ai = Hi * d

    I = I + Ai

print(I)