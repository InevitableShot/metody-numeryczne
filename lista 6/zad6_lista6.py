# Jakub Ignatowicz zadanie 6 lista 6
import numpy as np
from scipy.special import roots_legendre

# Definuje funkcje z zadania
def func(x):
    return ((np.log(x))/(x**2-2*x+2))

# Ustawiam granice calkowania z zadania
a = 1
b = np.pi

# Tworze petle dla kolejnych wezlow
for n in np.array([2, 4]):
    xi, ai = roots_legendre(n)  # Calke obliczam metoda Gaussa-Legendre'a
    I_n = 0
    for i in range(len(ai)):
        I_n += (b-a)/2*ai[i] * func((b+a)/2 + (b-a)/2*xi[i])    # Wzor z wykladu
    print(f"wezel = {n}\twynik = {I_n}")

