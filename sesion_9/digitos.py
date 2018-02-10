from sklearn import datasets

digits = datasets.load_digits()

X = digits.data # Caracteristicas
Y = digits.target # Etiquetas (el objetivo a clasificar)

print(X)
print(Y)

print("Datos de entrenamiento: {}".format(X.shape))

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier()

clf.fit(X, Y)

Xp = [[0, 0,  0, 16, 0, 0, 0, 0, 0, 0, 16, 16, 0, 0, 0, 0, 0, 0,  0, 16, 0, 0, 0, 0, 0, 0,  0, 16, 0, 0, 0, 0, 0, 0,  0, 16, 0, 0, 0, 0, 0, 0,  0, 16, 0, 0, 0, 0, 0, 0,  0, 16, 0, 0, 0, 0, 0, 0, 16, 16, 16, 0, 0, 0]]

Yp = clf.predict(Xp)

print("El digito es: {}".format(Yp))

from sklearn import svm, metrics
import matplotlib.pyplot as plt
import numpy as np

image = np.ndarray(Xp)

print(image)

# plt.subplot(2, 4, index + 1)
#     plt.axis('off')
#     plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
#     plt.title('Training: %i' % label)
#     print(image)

# plt.show()