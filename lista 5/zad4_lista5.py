# Jakub Ignatowicz zadanie 4 lista 5
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Dane z zadania
x = np.array([0.2, 2, 20, 200, 2000, 20000], dtype=float)
y = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433], dtype=float)

log_poly_lagrange = lagrange(x, y)      # dopasowuje funkcje korzystajac z metody lagrange

Re_to_find = [5.50, 5000]               # tablica wartosci Re dla ktorych szukamy wartosci cD

# znalezienie oraz wypisanie wartosci cD dla zadanego Re_1 i Re_2
cd = log_poly_lagrange(Re_to_find)
print(f'Dla Re - 5.5 \tcd = {cd[0]}')
print(f'Dla Re - 5000 \tcd = {cd[1]}')

# Dane potrzebne do wykresu
x_poly_2 = np.arange(0.2, 20001, 0.1)

# Wykres
plt.plot(x_poly_2, log_poly_lagrange(x_poly_2), 'b')
plt.plot(x, y, 'og')
plt.plot(Re_to_find, cd, 'or')          # drugiego punktu nie widac na wykresie poniewaz nie miesci sie w zakresie
plt.legend(['cD(Re) - dopasowana metoda lagrange', 'dane', 'znalezione cD'], loc='best')
plt.xscale('log')
plt.yscale('log')
plt.show()
