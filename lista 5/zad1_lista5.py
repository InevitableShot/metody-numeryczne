# Jakub Ignatowicz zadanie 1 lista 5
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Dane z zadania
h = np.array([0, 3, 6], dtype=float)
rho = np.array([1.225, 0.905, 0.652], dtype=float)


lagr = lagrange(h, rho)             # dopasowuje funkcje kwadratowa metoda lagrange
print(f'Wzor funkcji:\n{lagr}')     # wypisuje wzor dopasowanej funkcji

# Dane do wykresu
x2 = np.arange(-1, 7, 0.01)

# Wykres
plt.plot(x2, lagr(x2), 'b')
plt.plot(h, rho, 'og')
plt.legend(['funkcja kwadratowa - dopasowana metoda lagrange', 'dane'], loc='upper right')
plt.title(f'p(h) = {lagr.coef[0]:.6f} h^2 {lagr.coef[1]:.4f} h +{lagr.coef[2]:.3f}')
plt.xlabel('h')
plt.ylabel('p')
plt.show()
