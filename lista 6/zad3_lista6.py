# Jakub Ignatowicz zadanie 3 lista 6
import numpy as np
from scipy.interpolate import lagrange

# Dane z zadania
x = np.array([-2.2, -0.3, 0.8, 1.9])
y = np.array([-15.18, 10.962, 1.92, -2.04])

# Dopasowuje wielomian metoda lagrange
poly = lagrange(x, y)


poly_first_deriv = np.polyder(poly, 1)
print(f"f'(0) = {poly_first_deriv(0)}")
poly_second_deriv = np.polyder(poly, 2)
print(f"f''(0) = {poly_second_deriv(0)}")
