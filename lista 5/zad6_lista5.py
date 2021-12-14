# Jakub Ignatowicz zadanie 6 lista 5
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Dane z zadania
h = np.array([0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150], dtype=float)
p = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741], dtype=float)

# deklaruje postac funkcji ktora bede dopasowywal
def funq(x,a,b,c):
    return a*(x**2)+b*x+c

parm, pcov = curve_fit(funq,h,p)          #parm zawiera obliczone parametry a,b,c, uzywam funkcji curve_fit ktora stosuje metode najmniejszych kwadratow
print(f'{parm[0]:.6f}x^2 {parm[1]:.6f}x +{parm[2]:.6f}')

print("d na wysokości h - 10.5km = ", funq(10.5, *parm))


# Wykres
xx = np.arange(0, 22, 0.001)
plt.plot(xx, funq(xx, *parm), 'b')
plt.plot(h, p,'og')
plt.plot(10.5, funq(10.5, *parm), 'or')
plt.xlabel('h')
plt.ylabel('p')
plt.legend(['dopasowana funkcja kwadratowa', 'dane', 'rozwiazanie'], loc='upper right')
plt.title('Wykres do zadania 6')
plt.show()
