# Jakub Ignatowicz zadanie 5 lista 5
import numpy as np
import matplotlib.pyplot as plt

# Dane z zadania
x=np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7], dtype=float)
y=np.array([6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828], dtype=float)

func1 = np.polyfit(x,y, 1)
poly1=np.poly1d(func1)

func2 = np.polyfit(x,y, 2)
poly2=np.poly1d(func2)
xx=np.arange(0.0, 4, 0.01)


# Wykres
plt.plot(x, y,'og')
plt.plot(xx, poly1(xx), '')
plt.plot(xx, poly2(xx))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['dane', 'funkcja liniowa', 'funkcja kwadratowa'], loc='best')
plt.title('wykres do zadania 5')
plt.show()


# Funkcja kwadratowa jest lepiej dopasowana do tych danych, poniewaz punkty lepiej sie z nia pokrywaja na wykresie