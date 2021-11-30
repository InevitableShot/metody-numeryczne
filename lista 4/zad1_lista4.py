# Jakub Ignatowicz zadanie 1 lista 4
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def func(x):
    return 2*x**4+24*x**3+61*x**2-16*x+1

d = 0.0001      # przedzial, co jaki wykonujemy sprawdzenie miejsc zerowych (odleglosc pomiedzy a i b)
a = -9          # po przeanalizowaniu wykresu podaje poczatkowe a
roots = []      # pusta tablica na miejsca zerowe

# Funkcja dla x < -10 rosnie do +nieskonczonosci
# Funkcja dla x > 3 rośnie do +nieskonczonosci
# Dlatego miejsc zerowych szukam w przedziale x = [-10,3]
for b in np.arange(-10, 3, d):
    if np.sign(func(a)) != np.sign(func(b)):
        root = optimize.ridder(func, a, b, xtol=1e-14,rtol=9e-16, full_output=False)
        plt.plot(root, 0, 'o')
        roots.append(root)
    a = b

# Petla do wypisania miejsc zerowych
print("Miejsca zerowe funkcji wynosza:")
for i in range(len(roots)):
    print(f'x{i} = {roots[i]}')

# Ustawienia wykresu
x = np.arange(-10, 3, d)
plt.plot(x, func(x), color='m')
plt.axhline(y=0, color='k')         # wykreslam pozioma linie w y=0, aby miejsca zerowe byly lepiej widoczne
plt.grid()
plt.title('Wykres naszej funkcji z zadania 1')
plt.ylabel('y')
plt.xlabel('x')
plt.show()
# Na wykresie dwa miejsca zerowe sa bardzo blisko siebie i przy przyjetej skali wykresu nachodza na siebie,
# nalezy przyblizyc wykres wokol nich, aby faktycznie zobaczyc, ze sa to dwa osobne miejsca zerowe