# Jakub Ignatowicz zadanie 6 lista 5
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
dx = np.array([0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150], dtype=float)
dy = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741], dtype=float)

# najpierw deklarujemy postać funkcji, którą dopasujemy do danych
def funq(x,a,b,c):
    return a*(x**2)+b*x+c

parm1 , pcov = curve_fit(funq,dx,dy)
print(parm1)
#parm1 zawiera obliczone parametry a,b,c

plt.plot(dx, dy,'o')
xx=np.linspace(0, 11, num=100, endpoint=True)
plt.plot(xx, funq(xx,*parm1))
plt.plot(10.5, funq(10.5, *parm1), "ob")
print("P na wysokości h=10.5km = ", funq(10.5,*parm1))
plt.show()