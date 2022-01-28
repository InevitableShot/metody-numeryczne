# Jakub Ignatowicz zadanie 1 lista 8
import numpy as np
import scipy.linalg as slin

# Macierz z zadania
A = ([-1, -4, 1],
     [-1, -2, -5],
     [5, 4, 3])

# Otrzymuje wartosci wlasne oraz wektory wlasne za pomoca funkcji eig z scipy.linalg
values, vectors = slin.eig(A)

print(f"Wartosci wlasne: {np.round(values,6)}")
print(f"Wektory wlasne: ")
for vector in vectors:
    print(" ", np.round(vector, 8))

# Wyniki zaokraglam, aby pozbyc sie wynikow bliskich zeru oraz aby zwiekszyc czytelnosc wynikow