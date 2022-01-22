# Jakub Ignatowicz zadanie 3 lista 7
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Dane z zadania
g = 9.81        # Przyspieszenie ziemskie
cw = 0.35       # Wspolczynnik oporu powietrza
rho = 1.2       # Gestosc powietrza
m = 0.5         # Masa pilki (przyjmuje stala mase pilki = 0.5 kg)

# Funkcja potrzebna do obliczen z pominieciem oporow powietrza (podpunkt a)
def a(v0, alfa):
    time = (2 * v0 * np.sin(alfa * np.pi / 180.)) / g   # Obliczam czas lotu
    t = np.arange(0, time, 0.01)                        # Tworze tablice o dlugosci czasu lotu z przedzialem czasowym 0.01 s
    h = [(v0 * i * np.sin(alfa * np.pi / 180.)) - ((g * i ** 2) / 2) for i in t]    # Obliczam wysokosc na jakiej w danym czasie znajduje sie pilka
    return [t, h]   # Funkcja zwraca czas oraz wysokosc na jakiej polozona jest pilka

# Funkcja potrzebna do obliczen z uwzglednieniem oporow powietrza (podpunkt b)
def f(t, y, k):
    xdot = y[1]                             # Predkosc vx
    zdot = y[3]                             # Predkosc vy
    speed = np.hypot(xdot, zdot)            # Obliczam predkosc v
    xdotdot = -k / m * speed * xdot         # Zmiana predkosci vx
    zdotdot = -k / m * speed * zdot - g     # Zmiana predkosci vy
    return [xdot, xdotdot, zdot, zdotdot]   # Funkcja zwraca wszystkie potrzebne predkosci

# Funkcja sprawdzajaca czy pilka uderzyla juz w ziemie (osiagnela wysokosc 0)
def hit_ground(t, y, k):
    return y[2]


hit_ground.direction = -1       # Kierunek pilki musi byc ujemny, poniewaz pilka spada
hit_ground.terminal = True      # Jezeli warunek jest spelniony, zatrzymujemy obliczenia


# Funkcja do podpunktu drugiego
def b(v0, alfa, r):
    A = np.pi * r ** 2                      # Pole przekroju poprzecznego pilki
    k = 0.5 * cw * rho * A                  # Wzor z zadania na sile oporu powietrza
    vx = v0 * np.cos(alfa * np.pi / 180.)   # Predkosc poczatkowa vx
    vy = v0 * np.sin(alfa * np.pi / 180.)   # Predkosc poczatkowa vy
    result = solve_ivp(f, (0, 50), [0, vx, 0., vy], args=[k], dense_output=True, events = hit_ground) # Rozwiazuje rownanie rozniczkowe ruchu pilki
    return result

# Ustawiam przykladowe dane
v = [10, 15, 30]            # Predkosc pilki
r = [0.06, 0.11, 0.11]      # Promien pilki
angle = [30, 45, 60]        # Kat rzutu pilki


# Tworze okno z 3 podwykresami. po 1 wykresie na kazdy zbior danych
figure, axs = plt.subplots(3)

# Ustawiam wielkosc wykresu
figure.set_size_inches(20, 12)

# Petla sluzaca do obliczen oraz narysowania wykresu
for i in range(len(v)):
    # Obliczenia do podpunktu a
    z1 = a(v[i], angle[i])
   
    # Obliczenia do podpunktu b
    z2 = b(v[i], angle[i], r[i])
   
    # Ustawiam przedzial czasu
    t = np.linspace(0, z2.t_events[0][0], 1000)
    
    # Rysowanie wykresu
    axs[i].plot(z1[0], z1[1], label=f"Bez oporu\nv = {v[i]} m/s\nr = {r[i]} m\nkat = {angle[i]}\N{DEGREE SIGN}")
    axs[i].plot(t, z2.sol(t)[2], label=f"Z oporem\nv = {v[i]} m/s\nr = {r[i]} m\nkat = {angle[i]}\N{DEGREE SIGN}")
    axs[i].set_xlabel("t [s]")
    axs[i].set_ylabel("h [m]")
    axs[i].legend(loc = 'upper right')

plt.show()