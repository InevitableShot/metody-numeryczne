# Jakub Ignatowicz zadanie 4 lista 1
import numpy as np
from scipy import linalg as slin

# funkcja tworzaca macierz Hilberta o zadanej wielkosci n
def hilbert(n):
    H = np.zeros([n, n])
    for i in range(0, n):
        for k in range(0, n):
            H[i, k] = 1/(i+k+1)
    return H

# macierze dla n = 4
print(f"Macierz Hilberta dla n = 4\n{hilbert(4)}\n")
print(f"Macierz odwrotna do macierzy Hilberta dla n = 4\n{slin.inv(hilbert(4))}\n")

# macierze dla n = 8
print(f"Macierz Hilberta dla n = 8\n{hilbert(8)}\n")
print(f"Macierz odwrotna do macierzy Hilberta dla n = 8\n{slin.inv(hilbert(8))}\n")

# wyznaczniki macierzy Hilberta dla n = [5,20]
print(f"Wyznaczniki macierzy Hilberta dla n = [5,20]")
for n in range(5, 21):
    print(f"n = {n} \t=\t {slin.det(hilbert(n))}")
