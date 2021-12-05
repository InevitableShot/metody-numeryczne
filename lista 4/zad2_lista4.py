# Jakub Ignatowicz zadanie 2 lista 4
import numpy as np
import matplotlib.pyplot as plt


def newton(x_1, a, accuracy=24):
    x = [x_1]
    for i in range(accuracy-1):
        x.append(x[i] - f_0(x[i], a)/f_1(x[i]))
    return x[accuracy-1]


def f_0(x, a):
    return (x**5 - a)


def f_1(x):
    return (5 * x**4)


n = float(input('Podaj dowolna liczbe dodatnia: '))
predicted = float(input('Podaj przewidywana wartosc wyniku pierwiastka 5-tego stopnia z tej liczby: '))
print(f'Pierwiastek piątego stopnia z liczby {n} = {newton(predicted, n)}')

# Jesli nasz przewidywany wynik bedzie w miare prawdopodobny, to nasz obliczony wynik bedzie poprawny