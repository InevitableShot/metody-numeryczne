# Jakub Ignatowicz zadanie 4 lista 3
import numpy as np
from scipy import linalg as slin

# Do rozwiazania tego zadania posluze sie metoda eliminacji Gaussa, a wiec rozwiaze uklad y = ax, gdzie szukamy wspolczynnikow a

# macierz x-ow, podstawiam wartosci kolejnych x-ow (z kolejnych punktow nalezacych do wielomianu) dla kazdego wspolczynika a (1 w pierwszej kolumnie, poniewaz przy a0 nie stoi zaden x)
x = np.array([[1, 0, 0, 0, 0],          # dla x = 0
             [1, 1, 1, 1, 1],           # dla x = 1
             [1, 3, 9, 27, 81],         # dla x = 3
             [1, 5, 25, 125, 625],      # dla x = 5
             [1, 6, 36, 216, 1296]])    # dla x = 6

# macierz y-ow, podstawiam wartosci kolejnych y-ow (z kolejnych punktow nalezacych do wielomianu)
y = np.array([[-1], [1], [3], [2], [-2]])

# za pomoca funkcji solve z modulu linalg z biblioteki scipy rozwiazuje uklad rownan, funkcja wykorzystuje do tego eliminacje Gaussa
a = slin.solve(x, y)
print(f"a0 = {a[0][0]}\ta1 = {a[1][0]}\ta2 = {a[2][0]}\ta3 = {a[3][0]}\ta4 = {a[4][0]}")
# wyniki wychodza poprawne, sprawdzilem je na kalkulatorze podstawiajac kolejne punkty do wielomianu z wyliczonymi wspolczynnikami
