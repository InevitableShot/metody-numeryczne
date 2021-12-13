# Jakub Ignatowicz zadanie 4 lista 5
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.array([0.2, 2, 20, 200, 2000, 20000], dtype = float)
y = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433], dtype = float)

log_poly_lagrange = lagrange(np.log(x), np.log(y))

plt.plot(x,y,'o')

x_poly_2 = np.arange(0.2, 20000, 1)

x_poly = [5, 50, 5000]
c_d = np.exp(log_poly_lagrange(np.log(x_poly)))
print(f'c_d = {c_d}')

plt.plot(x_poly, c_d, 'og')
plt.plot((x_poly_2), np.exp(log_poly_lagrange(np.log(x_poly_2))))
plt.legend(['dane',  'log_poly_lagrange'], loc='best')
plt.xscale('log')
plt.yscale('log')
plt.show()