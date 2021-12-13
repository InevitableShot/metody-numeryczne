# Jakub Ignatowicz zadanie 3 lista 5
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0.2, 2, 20, 200, 2000, 20000])
y = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433])

log_x = np.log(x)
log_y = np.log(y)

log_cubic_spline = CubicSpline(log_x, log_y)

x_poly = [5, 50, 5000]
c_d = np.exp(log_cubic_spline(np.log(x_poly)))
print(f'c_d = {c_d}')

x_poly_2 = np.arange((0.2), (20000), 1)
d2 = np.exp(log_cubic_spline(np.log(x_poly_2)))

plt.plot(x,y,'o')
plt.plot(x_poly, c_d, 'og')
plt.plot(x_poly_2,d2)
plt.xscale('log')
plt.yscale('log')
plt.show()