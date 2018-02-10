from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

X = [
    [1, 1, 0],
    [0, 0, 1],
]

Y = [
    [0],
    [1]
]

clf.fit(X, Y)

Xp = [
    [1, 1, 1],
    [0, 1, 1]
]

Yp = clf.predict(Xp)

print(Yp)