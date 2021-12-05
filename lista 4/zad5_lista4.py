# Jakub Ignatowicz zadanie 5 lista 4
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def draw_line():
    # wspolrzedne koszykarza
    x_k = [0, 0]
    y_k = [0, 2]
    plt.plot(x_k, y_k, linewidth=3)

    # wspolrzedne kosza
    x_kosz = [9.5, 10.5]
    y_kosz = [3, 3]
    plt.plot(x_kosz, y_kosz, linewidth=3)


def throw(x, y, a, v, vy):
    for t in np.arange(0.0, 10.0, 0.01):
        g = 9.81
        x_p = v*np.cos(a)*t
        y_p = 2+v*np.sin(a)*t-((g*t*t))/2
        if x_p <= 10.0:                     # jesli punkt x jest mniejszy niż 10 dodaje do listy
            x.append(x_p)
            y.append(y_p)
            vy.append(v*np.sin(a)-(g*t))
        else:
            break


def check(v, a, vy):
    vx = v*np.cos(a)
    if (2.95 <= y[-1] <= 3.05) and (0.95 <= (np.abs(vy[-1]/vx)) <= 1.05):
        print(f"v_0 = {v}\nkat alfa = {np.rad2deg(a)}")
        return False
    else:
        return True


draw_line()

ff = True
for v in np.arange(10, 11, 0.1):
    for alpha in np.arange(10, 90, 0.1):
        if ff is True:
            a = np.deg2rad(alpha)
            x = []                      # dlugosc
            y = []                      # wysokosc
            vy = []                     # predkosc y w danej chwili
            throw(x, y, a, v, vy)
            ff = check(v, a, vy)


plt.plot(x, y, linewidth=3)
plt.title('Wykres naszej funkcji z zadania 5')
plt.ylabel('y')
plt.xlabel('x')
plt.grid()
plt.show()
