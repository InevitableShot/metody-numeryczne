# Jakub Ignatowicz zadanie 6 lista 4
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def functions(x):
    return [np.tan(x[0])-x[1]-1, np.cos(x[0])-(3*np.sin(x[1]))]


result = []
e = 4
for i in np.arange(0, 3, 0.01):
    for j in np.arange(0, 3, 0.01):
        x1 = optimize.root(functions, [j, i])
        if x1.success:
            if 0 <= round(x1.x[0], e) <= 1.5:
                if [round(x1.x[0], e), round(x1.x[1], e)] not in result:
                    result.append([round(x1.x[0], e), round(x1.x[1], e)])
                    plt.plot((round(x1.x[0], e)),
                             (round(x1.x[1], e)), 'o', color='r')

for i in range(len(result)):
    print(f'Rozwiazanie {i+1}: \n\t\t x= {result[i][0]}\n\t\t y= {result[i][1]}')

x = np.arange(0.0, 1.5, 0.0001)
y = np.tan(x)-1
plt.plot(x, y)
z = np.cos(x)/3
for i in range(0, 5):
    plt.plot(x, np.sin(z)+(3.14*i))

# Ustawienia wykresu
plt.title('Wykres naszych funkcji z zadania 6')
plt.ylabel('y')
plt.xlabel('x')
plt.axis('equal')
plt.grid()
plt.show()
