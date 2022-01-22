# Jakub Ignatowicz zadanie 1 lista 7
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Rownanie z zadania
def func(t, y): 
    return np.sin(t * y)

# Dane z zadania
y = [2, 2.5, 3, 3.5]
t = [0, 6]

# Petla po kazdym elemencie z tablicy y-ow
for element in y:
    result = solve_ivp(func, t, [element], atol = 1e-12, rtol = 1e-9)   # Rozwiazuje rownanie rozniczkowe dla poszczegolnego y z petli
                                                                        # Okreslam tolerancje atol oraz rtol w celu otrzymania wiekszej ilosci wynikow
    plt.plot(result.t, result.y[0], 'o-')                               # Wykreslam kolejne rozwiazania dla poszczegolnego y z petli

# Ustawienia wykresu
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['y0 = 2', 'y0 = 2.5', 'y0 = 3', 'y0 = 3.5'])
plt.title('Wykres z zadania 1')
plt.show()