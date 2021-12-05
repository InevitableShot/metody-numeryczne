# Jakub Ignatowicz zadanie 4 lista 4
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def f_1(x, y):
    return (x + np.exp(-x) + y**3)


def f_2(x, y):
    return (x**2 + 2*x*y - y**2 + np.tan(x))


def func(x):
    return [f_1(x[0], x[1]), f_2(x[0], x[1])]


# Funkcje potrzebne tylko do wykresow
def f_1_r(x): return np.cbrt(-np.exp(-x) - x)
def f_2_r_1(x): return (x - np.sqrt(2 * x**2 + np.tan(x)))
def f_2_r_2(x): return (x + np.sqrt(2 * x**2 + np.tan(x)))
def f_o_1(x, r=2): return np.sqrt(r**2 - x**2)
def f_o_2(x, r=2): return -np.sqrt(r**2 - x**2)


# Przewidywane wartosci miejsc zerowych na podstawie wykresu
x0s = [
    np.array([-1.271, -1.269]),
    np.array([-0.714, -0.71]),
    np.array([1.2066, 1.2068]),
]

index = 1
for x0 in x0s:
    x1 = optimize.root(func, x0)
    if x1.success:
        print(f'Rozwiazanie {index}:\n\t\tx = {x1.x[0]} \n\t\ty = {x1.x[1]}')
        plt.plot(x1.x[0], x1.x[1], 'or')
        index += 1


x = np.linspace(-2, 2, 1000000)

plt.axis([-2, 2, -2, 2])

# Rysuje okrag o promieniu 2 i srodku w [0,0]
plt.plot(x, f_o_1(x), color='b')
plt.plot(x, f_o_2(x), color='b')

# Rysuje funkcje
plt.plot(x, f_1_r(x), color='m')
plt.plot(x, f_2_r_1(x), color='g')
plt.plot(x, f_2_r_2(x), color='g')

# Ustawienia wykresu
plt.title('Wykres naszej funkcji z zadania 4')
plt.ylabel('y')
plt.xlabel('x')
plt.show()
