# Jakub Ignatowicz zadanie 2 lista 1
import matplotlib.pyplot as plt
import numpy as np

x = [0.1] # poczatkowa wartosc w liscie

for i in range(0, 99): # petla wyliczajaca i dodajaca kolejne wartosci ciagu do listy
    x.append(3.5 * x[i] * (1 - x[i]))

plt.scatter([i for i in range(0, 100)], x)
plt.xlabel("n")
plt.ylabel("x")
plt.xticks(np.arange(0, 101, 5))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.show()
