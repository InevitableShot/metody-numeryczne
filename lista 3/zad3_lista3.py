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

print(f"x = {slin.solve(A,b)}")
