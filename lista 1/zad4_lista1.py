# Jakub Ignatowicz zadanie 4 lista 1
import numpy as np
import matplotlib as plt
from scipy import linalg as slin

n = 4
h = np.zeros([n,n])
for i in range(0,n):
    for k in range(0,n):
        h[i, k] = 1/(i+k+1)
print(h)

n = 8
h = np.zeros([n,n])
for i in range(0,n):
    for k in range(0,n):
        h[i, k] = 1/(i+k+1)
print(h)

for n in range(1,21):
    h = np.zeros([n,n])
    for i in range(0, n):
        for k in range(0, n):
            h[i, k] = 1/(i+k+1)
    print(f"det {n} = {np.linalg.det(h)}")