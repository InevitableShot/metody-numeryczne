# Jakub Ignatowicz zadanie 2 lista 6
import numpy as np
from scipy.interpolate import lagrange

# Dane z zadania
x = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
y = np.array([0.0, 0.078348, 0.13891, 0.192916, 0.244981])

# Dopasowuje wielomian metoda lagrange, poniewaz punkty sa rownomiernie od siebie oddalone
poly = lagrange(x, y)

poly_deriv = np.polyder(poly, 1)
print(f"f'(0.2) = {poly_deriv(0.2)}")