# Jakub Ignatowicz zadanie 3 lista 1
import numpy as np
import scipy as sp

A = np.array([[4, -2, 1],
              [-2, 4, -2],
              [1, -2, 4]])

B = np.array([[4, 2, 0],
              [2, 5, 2],
              [0, 2, 4]])

w = np.array([[1],
              [-2],
              [3]])

print(f"AB = {np.matmul(A,B)}")
print(f"Aw = {np.matmul(A,w)}")
print(f"B(Aw) = {np.matmul(B,np.matmul(A,w))}")
print(f"det A = {np.round(np.linalg.det(A))}")
print(f"det B = {np.round(np.linalg.det(B))}")
print(f"A^-1 = {np.linalg.inv(A)}")
print(f"B^-1 = {np.linalg.inv(B)}")
