# Jakub Ignatowicz zadanie 1 lista 1
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1.5, 0.001)  # deklaruje przedzial x-ow
y = np.cos(x) - 3 * np.sin(np.tan(x) - 1)  # wyliczam y-ki na podstawie x-ow

x0 = 0  # zmienna na ilosc miejsc zerowych
for i in range(len(x)):  # petla sluzaca do obliczenia ilosci miejsc zerowych
    # 1 warunek sprawdza czy nie wyjdziemy poza zakres, 2 warunek sprawdza czy liczby sa przeciwnych znakow
    if (i+1) < len(x) and (y[i]*y[i+1]) < 0:
        x0 += 1  # jezeli liczby sa przeciwnych znakow zwiekszam ilosc miejsc zerowych o jeden

print(f"Ilość miejsc zerowych = {x0}")

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.xticks(np.arange(0, 1.6, 0.1))
plt.yticks(np.arange(-3, 4.1, 0.5))
plt.title("cos(x) - 3sin(tg(x) - 1)")
plt.show()
