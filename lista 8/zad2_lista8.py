# Jakub Ignatowicz zadanie 2 lista 8
import numpy as np
import scipy.linalg as slin

# Tworze macierz Hilberta o wielkosci 6x6
H = slin.hilbert(6)

# Otrzymuje wartosci wlasne oraz wektory wlasne za pomoca funkcji eig z scipy.linalg
values, vectors = slin.eig(H)


print(f"Wartosci wlasne: {values}")
print(f"Wektory wlasne: ")
for vector in vectors:
    print(" ", vector)