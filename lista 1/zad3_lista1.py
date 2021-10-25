# Jakub Ignatowicz zadanie 3 lista 1
import numpy as np
from scipy import linalg as slin

A = np.array([[4, -2, 1],
              [-2, 4, -2],
              [1, -2, 4]])

B = np.array([[4, 2, 0],
              [2, 5, 2],
              [0, 2, 4]])

w = np.array([[1],
              [-2],
              [3]])

print(f"AB = \n{np.matmul(A,B)}")
print(f"Aw = \n{np.matmul(A,w)}")
print(f"B(Aw) = \n{np.matmul(B,np.matmul(A,w))}")
print(f"det A = {slin.det(A)}")
print(f"det B = {slin.det(B)}")
print(f"A^-1 = \n{slin.inv(A)}")
print(f"B^-1 = \n{slin.inv(B)}")