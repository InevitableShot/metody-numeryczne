# Jakub Ignatowicz zadanie 1 lista 6
import numpy as np
from scipy.misc import derivative

# Definuje funkcje z zadania
def f(x):
    return np.log(np.tanh(x/(x**2+1)))

# Dana z zadania
x = 0.2

np1_5 = derivative(f, x, dx=0.0001, n=1, order=5)   # Ustawiam order = 5, poniewaz ilosc 5 punktow jest najbardziej odpowiednia dla naszego zadania
np2_5 = derivative(f, x, dx=0.0001, n=2, order=5)
np3_5 = derivative(f, x, dx=0.0001, n=3, order=5)
print(f"h = {0.0001}")
print(f"f'({x}) = {np1_5}")
print(f"f''({x}) = {np2_5}")
print(f"f'''({x}) = {np3_5}")

# Dla wartosci h = 0.0001 obliczone pochodne maja najwieksza dokladnosc, doszedlem do tego testujac kolejne wartosci
# i sprawdzajac je z wynikiem na wolfram alpha, nie nalezy przesadzac ze zbyt mala wartoscia h, poniewaz w pewnym momencie,
# nasze bledy zaczynaja rosnac zamiast malec i dzieje sie tak przy h = 0.00001