# Jakub Ignatowicz zadanie 7 lista 6
import numpy as np
from scipy.special import roots_legendre

# Definuje funkcje z zadania
def func(x):
    return ((np.cos(x) - np.exp(x)) / (np.sin(x)))


# Obliczam wartosc calki w wolframie alpha do 20 miejsca po przecinku
# https://www.wolframalpha.com/input/?i=SetPrecision%5Bintegral+%28%28cos%28x%29-e%5Ex%29%2Fsin%28x%29%29+from+-1+to+1%2C20%5D
iex = -2.2465917207286123514

# Ustawiam granice calkowania z zadania
a = -1
b = 1

for n in np.arange(2, 19, 2):
    xi, ai = roots_legendre(n)
    I_n = 0
    for i in range(len(ai)):
        I_n += (b-a)/2*ai[i] * func((b+a)/2 + (b-a)/2*xi[i])
    print(f"n = {n}\t wynik = {np.around(I_n,decimals=10)}\t blad = {iex - I_n}")

# Dla n rownego 8 wynik juz jest wystarczajaco dokladny