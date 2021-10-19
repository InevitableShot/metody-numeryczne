# Jakub Ignatowicz zadanie 2 lista 1
import matplotlib.pyplot as plt

x = [0.1]

for i in range(0, 99):
    x.append(3.5 * x[i] * (1 - x[i]))

plt.scatter([i for i in range(0, 100)], x)
plt.show()
