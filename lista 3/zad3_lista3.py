# Jakub Ignatowicz zadanie 3 lista 3
import numpy as np
from scipy import linalg as slin

# macierz A
A = np.array([[0, 0, 2, 1, 2],
              [0, 1, 0, 2, -1],
              [1, 2, 0, -2, 0],
              [0, 0, 0, -1, 1],
              [0, 1, -1, 1, -1]])

# wektor b
b = np.array([[1],
              [1],
              [-4],
              [-2],
              [-1]])

x = slin.solve(A,b)  # uzywam funkcji solve z modulu linalg z biblioteki scipy, wedlug polecenia, funkcja ta rozwiazuje uklad rownan Ax=b, uzywajac do tego metody eliminacji Gaussa
print(f"x1 = {x[0][0]}\tx2 = {x[1][0]}\tx3 = {x[2][0]}\tx4 = {x[3][0]}\tx5 = {x[4][0]}")
# Wyniki wychodza poprawne
