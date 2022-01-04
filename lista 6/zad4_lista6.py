# Jakub Ignatowicz zadanie 4 lista 6
import numpy as np
from scipy.integrate import simpson

# Definuje funkcje z zadania
def func(x):
    return np.cos(2/np.cos(x))

# Ustawiam granice calkowania z zadania
a = -1
b = 1

# Obliczam wartosc calki w wolframie alpha do 20 miejsca po przecinku
# https://www.wolframalpha.com/input/?i=SetPrecision%5Bintegral+%28cos%282%2Fcos%28x%29%29%29+from+-1+to+1%2C20%5D
value = -1.3655444514185000049 


# Petla po kolejnych wezlach
for w in np.array([3, 5, 7]):
    x = np.linspace(a, b, num=w)
    y = func(x)
    result = simpson(y, x)
    print(f"wezel =  {w}\twynik = {result}\tblad = {abs(value-result)}")

# Kolejne wezly zmniejszaja nam blad jakim obarczony jest wynik, jednakze tak bedzie tylko do pewnego momentu,
# dlatego ilosc wezlow nalezy dopasowywac z rozwaga