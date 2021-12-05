# Jakub Ignatowicz zadanie 3 lista 1
import numpy as np
from scipy import linalg as slin

# macierz A
A = np.array([[4, -2, 1],
              [-2, 4, -2],
              [1, -2, 4]])

# macierz B
B = np.array([[4, 2, 0],
              [2, 5, 2],
              [0, 2, 4]])

# wektor w
w = np.array([[1],
              [-2],
              [3]])

print(f"AB = \n{np.matmul(A,B)}\n")  # mnozenie A z B
print(f"Aw = \n{np.matmul(A,w)}\n")  # mnozenie A z w
print(f"B(Aw) = \n{np.matmul(B,np.matmul(A,w))}\n") # mnozenie B z wymnozonym A z w
print(f"det A = {slin.det(A)}")  # wyznacznik macierzy A
print(f"det B = {slin.det(B)}\n")  # wyznacznik macierzy B
print(f"A^-1 = \n{slin.inv(A)}\n")  # macierz odwrotna do macierzy A
print(f"B^-1 = \n{slin.inv(B)}")  # macierz odwortna do macierzy B
