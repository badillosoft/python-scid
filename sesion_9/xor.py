X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
]

Y = [
    0,
    1,
    1,
    0
]

from sklearn.tree import DecisionTreeClassifier

clf_1 = DecisionTreeClassifier()

clf_1.fit(X, Y)

from sklearn.neural_network import MLPClassifier

clf_2 = MLPClassifier(hidden_layer_sizes=(100, 200))

clf_2.fit(X, Y)

X1 = []
X2 = []
C_1 = []
C_2 = []

for x2 in range(0, 101):
    x2 = x2 / 100.
    for x1 in range(0, 101):
        x1 = x1 / 100.

        y_1 = clf_1.predict([[x1, x2]])[0] # [y] => [y][0] = y
        y_2 = clf_2.predict([[x1, x2]])[0]

        X1.append(x1)
        X2.append(x2)

        C_1.append(y_1)
        C_2.append(y_2)

        # print("{} {} {}".format(x1, x2, y))

import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=1, ncols=2)

ax[0].scatter(X1, X2, c=C_1)
ax[1].scatter(X1, X2, c=C_2)

plt.show()