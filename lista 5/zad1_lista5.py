# Jakub Ignatowicz zadanie 1 lista 5
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange


x = np.array([0, 3, 6], dtype=float)
w = np.array([1.225, 0.905, 0.652], dtype=float)
lagr = lagrange(x, w)
print(lagr)

# Ustawienia wykresu
x2 = np.arange(-25, 25, 0.01)
plt.plot(x, w, 'o')
plt.plot(x2, lagr(x2))
plt.legend(['dane', 'funkcja kwadratowa metoda lagrange'], loc='upper right')
plt.title(f'{lagr.coef[0]:.6f}x^2 {lagr.coef[1]:.4f}x +{lagr.coef[2]:.3f}')
plt.show()