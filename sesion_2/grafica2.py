import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5, 6, 7, 8], [10, 5, 3, 2, 6, 7, 8, 2], "m-+")
plt.plot([1, 2, 3, 4, 5, 6, 7, 8], [8, 6, 4, 1, 5, 8, 14, 5], "c-*")

plt.grid()

plt.savefig("g2.png")