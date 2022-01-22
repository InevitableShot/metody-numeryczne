# Jakub Ignatowiicz zadanie 4 lista 7
import numpy as np
from scipy.integrate import solve_ivp
from scipy import optimize
import matplotlib.pyplot as plt

# Warunki brzegowe ustalone w zadaniu
ya = 0
tk = np.pi
yb = 0

# Zapisuje rownanie rozniczkowe z zadania
def f(t, y):
    return [y[1], -np.sin(y[0]) - 1]

# Funkcja obliczajaca wartosc na 2 brzegu
def f1(y):
    return solve_ivp(f, [0, tk], [ya, y], dense_output=True).y[0, -1] - yb

# Szukam wartosci rozwiazania na 2 brzegu
opt = optimize.newton(f1, 0)

# Rozwiazuje rownanie rozniczkowe z zadania, znajac wartosc na 2 brzegu
w = solve_ivp(f, [0, tk], [ya, opt], atol=1e-12, rtol=1e-9, dense_output=True)

# Zaznaczam pierwsza wartosc brzegowa
plt.plot(tk, 0,'o', label="1 wartosc brzegowa")
# Zaznaczam druga wartosc brzegowa
plt.plot(ya, yb,'o', label="2 wartosc brzegowa")
# Rysuje rozwiazanie rownania rozniczkowego z zadania
plt.plot(w.t, w.y[0], '-', label='rozwiazanie')

# Ustawienia wykresu
plt.xlabel("t")
plt.ylabel("y")
plt.title('Wykres z zadania 4')
plt.legend()
plt.show()
