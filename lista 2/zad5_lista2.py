# Jakub Ignatowicz zadanie 5 lista 2
import numpy as np

# Funkcja rekurencyjna, która pomaga nam w obliczeniu całki
def I(n):
    if n <= 1:
        return 1
    else:
        return np.exp(1) - (n * I(n-1))

for n in range(2, 21):
    print(f"n = {n}\t wynik calki = {I(n)}")

# Wynik dla n = 16 już jest obarczony błędem rzędu 0.001, natomiast wyniki od 18 w górę są już kompletnie niepoprawne,
# ponieważ kolejne wyniki powinny dążyć coraz bliżej zera