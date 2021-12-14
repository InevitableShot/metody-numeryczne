# Jakub Ignatowicz zadanie 3 lista 5
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Dane z zadania
Re = np.array([0.2, 2, 20, 200, 2000, 20000], dtype=float)
cd = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433], dtype=float)


y = CubicSpline(Re, cd)                             # dopasowuje funkcje korzystajac z naturalnej funkcji sklejanej - CubicSpline

Re_to_find = [5.50, 5000]                           # tablica wartosci Re dla ktorych szukamy wartosci cD

# znalezienie oraz wypisanie wartosci cD dla zadanego Re_1 i Re_2
print(f'Dla Re - {Re_to_find[0]}\t cD = {y(Re_to_find[0])}')
print(f'Dla Re - {Re_to_find[1]}\t cD = {y(Re_to_find[1])}')

# wartosci potrzebne do narysowania wykresu
x = np.arange(0, 20001, 0.1)
y1 = y(x)

# Wykres
plt.plot(x, y1, 'b')
plt.plot(Re, cd, 'og')
plt.plot(Re_to_find, y(Re_to_find), 'or')           # drugiego punktu nie widac na wykresie poniewaz nie miesci sie w zakresie
plt.legend(['cD(Re) - dopasowana metoda CubicSpline', 'dane', 'rozwiazania'], loc='upper left')
plt.title("Wspolczynnik oporu cD jako funkcja liczby Re")
plt.xlabel("Re")
plt.ylabel("cD")
plt.xscale('log')                                   # ustawiam skale logarytmiczna dla x-ow
plt.yscale('log')                                   # ustawiam skale logarytmiczna dla y-ow
plt.show()
