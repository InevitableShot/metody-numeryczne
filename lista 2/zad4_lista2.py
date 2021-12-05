# Jakub Ignatowicz zadanie 4 lista 2
import numpy as np

# Funkcja zwraca wartości dla pierwszego wyrażenia
def eq1(x):
    return np.sqrt(np.float32((x**4)+4))-2

# Funkcja zwraca wartości dla drugiego wyrażenia, skorzystałem z przekształcenia wzoru z poprzedniego zadania
def eq2(x):
    return (x**4)/(np.sqrt(np.float32((x**4)+4))+2)

for n in range(0,25):
    x = 2 ** (-n)
    print("x =", x)
    print("Wzor 1:", eq1(x))
    print("Wzor 2:", eq2(x), "\n")

# Korzystając z wyrażenia drugiego, które jest równoważne do pierwszego otrzymujemy poprawne wyniki
# oraz są one obarczone dużo mniejszym błędem