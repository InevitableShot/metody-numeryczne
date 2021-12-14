# Jakub Ignatowicz zadania 2 lista 5
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Dane z zadania
x = np.array([1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3], dtype=float)
y = np.array([-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334], dtype=float)


cubic = CubicSpline(x, y)                   # dopasowuje funkcje korzystajac z naturalnej funkcji sklejanej - CubicSpline
print(f"y'(2.1) = {cubic(2.1, 1)}")         # wypisuje wartosc pierwszej pochodnej dla x = 2.1

# metoda roots pozwala nam obliczyc pierwiastki z dopasowanej wczesniej funkcji
# obcinam pierwszy oraz ostatni znaleziony pierwiastek, poniewaz funkcja "odgina sie" poza zakresem punktow z zadania,
# a wiec przy wiekszej ilosci punktow w zadaniu prawdopodobne byloby ze tych miejsc zerowych by tam nie bylo, lub bylyby w innym miejscu
# zostawiam tylko miejsca zerowe ktore zawieraja sie w przedziale punktow z zadania
roots_x = cubic.roots()[1:-1]               
print(f'Pierwiastki funkcji: {roots_x}')    # wypisuje znalezione pierwiastki

# Wykres
plt.plot(x, y, 'og')
x_poly = np.arange(0.9, 3.1, 0.01)
plt.plot(x_poly, cubic(x_poly), 'b')
plt.plot(roots_x, np.zeros(len(roots_x)), "or")
plt.axhline(y=0, color='k')                 # wykreslam pozioma linie w y=0, aby miejsca zerowe byly lepiej widoczne
plt.grid()
plt.legend(['dane','wielomian - dopasowany metoda CubicSpline ', 'pierwiastki'], loc='best')
plt.title('Wykres wielomianu dopasowanego do danych')
plt.xlabel('x')
plt.ylabel('y')
plt.show()