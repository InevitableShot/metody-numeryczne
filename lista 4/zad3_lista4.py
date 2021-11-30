# Jakub Ignatowicz zadanie 3 lista 4
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

u = 2510.0                          # predkosc spalin wzgledem rakiety
M_0 = 2.8 * (10**6)                 # masa rakiety w momencie oderwania od Ziemi
m = 13.3 * (10**3)                  # szybkosc zuzycia paliwa
g = 9.81                            # przyspieszenie ziemskie

# Funkcja zwraca wartosci predkosci od czasu, wzor podany w zadaniu
# Od wzoru odejmuje 335, poniewaz taka jest wartosc predkosci dzwieku, jaka chcemy osiagnac,
# a za pomoca funkcji optimize.newton szukamy miejsca zerowego funkcji,
# dlatego musimy obnizyc wartosci funkcji o wartosc tej predkosci
def func(t):
    return u*np.log(M_0/(M_0-m*t))-g*t-335


print(f'Czas po jakim rakieta osiagnie predkosc dzwieku wynosi = {optimize.newton(func,10)} s')

# Ustawienia wykresu
t = np.arange(0, 80, 0.01)
plt.plot(optimize.newton(func, 0), 0, 'or')      # zaznaczam na wykresie miejsce zerowe, czyli nasze rozwiazanie zadania
plt.plot(t, func(t),'b')
plt.grid()
plt.title('Wykres predkosci rakiety od czasu')
plt.ylabel('v[m/s]')
plt.xlabel('t[s]')
plt.show()
