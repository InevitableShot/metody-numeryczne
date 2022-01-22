# Jakub Ignatowicz zadanie 2 lista 7
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Dane
g = 9.81                # Przyspieszenie ziemskie
l = 0.5                 # Przyjmuje dlugosc wahadla = 0.5 m 
w0 = np.sqrt(g / l)

# Dane z poszczegolnych podpunktow
Q = [2, 2, 2]
w = [2.0 / 3.0, 2.0 / 3.0, 2.0 / 3.0]
A = [0.5, 0.5, 1.35]
O = [0.01, 0.3, 0.3]

# Okreslam przedzial czasu
t = np.arange(0, 20, 0.01)

# Zapisuje rownanie rozniczkowe z zadania
def f(t, y, q, w, A):
    return [y[1], -y[1] / q - np.sin(y[0]) + A * np.cos(w * t)]

# Rozwiazuje rownanie rozniczkowe dla wszystkich podanych danych z kazdego podpunktu, uzywam do tego list comprehension aby skrocic zapis
result = [solve_ivp(f, [0, 20 * w0], [0, O[i]], args=[Q[i], w[i], A[i]], dense_output = True, t_eval = t * w0) for i in range(len(Q))]

# Tworze okno z 6 podwykresami, po 2 podwykresy dla kazdego podpunktu z danymi
figure, graphs = plt.subplots(2, 3)

# Ustawiam wielkosc wykresu
figure.set_size_inches(20, 12)

# Petla sluzaca do narysowania wykresow
for i in range(len(Q)):
    # Wykreslam wykresy zaleznosci theta od czasu
    graphs[0][i].plot(result[i].t, result[i].y[0], label = f'theta = {O[i]}\nQ = {Q[i]}\nw = {w[i]:.2f}\nA = {A[i]}\n')
    graphs[0][i].set_title('Zaleznosc theta (t)')
    graphs[0][i].set_xlabel('t')
    graphs[0][i].set_ylabel('theta')
    graphs[0][i].legend(loc = 'upper right')  
    
    # Wykreslam wykresy trajektorii w przetrzeni fazowej (theta', theta)
    graphs[1][i].plot(result[i].y[1], result[i].y[0], label = f'theta = {O[i]}\nQ = {Q[i]}\nw = {w[i]:.2f}\nA = {A[i]}\n')
    graphs[1][i].set_title("Trajektoria w przestrzeni fazowej (theta', theta)")
    graphs[1][i].set_xlabel('theta')
    graphs[1][i].set_ylabel("theta'")
    graphs[1][i].legend(loc = 'upper right')


plt.show()