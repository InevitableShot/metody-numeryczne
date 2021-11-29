# Jakub Ignatowicz zadanie 2 lista 4
import numpy as np
import matplotlib.pyplot as plt

def newton(x_1, a, accuracy = 24):
    x = []
    x.append(x_1)
    for i in range(accuracy-1):
        x.append(x[i] - f_0(x[i], a)/f_1(x[i]))
    return x[accuracy-1]

def f_0(x, a): return (x**5 - a)
def f_1(x): return (5 * x**4)

if __name__ == '__main__':
    print(f'2^(1/5) = {newton(0.5, 32)}')

    x = np.linspace(-3, 3, 1024)
    plt.plot(x, f_0(x, 32), color='r')
    plt.axhline(y=0,color='k')

    plt.show()