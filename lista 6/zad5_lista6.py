# Jakub Ignatowicz zadanie 5 lista 6
import numpy as np
from math import radians, degrees
from scipy.integrate import quad

# Definuje funkcje z zadania
def h(theta, theta0):
    return (1/np.sqrt(1-np.sin(theta0/2)**2*np.sin(theta)**2))


for angle in [radians(0), radians(15), radians(30), radians(45)]:
    result, err = quad(h, 0, np.pi/2, args=angle)
    print(
        f"h({np.round(degrees(angle),1)}) = {result}\troznica = {np.abs((np.pi/2)-result)}")

# Otrzymany wynik porownuje z wartoscia z zadania h(0) = pi/2 stosowana w przyblizeniu harmonicznym
# jak widac po kolejnych wynikach im wiekszy kat tym wieksza jest roznica w naszym wyniku
# Dodatkowo obliczylem wynik dla h(0), jak widac jego wynik pokrywa sie z tym podanym w zadaniu