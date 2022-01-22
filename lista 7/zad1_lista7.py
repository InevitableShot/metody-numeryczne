# Jakub Ignatowicz zadanie 1 lista 7
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def func(t, y): 
    return np.sin(t * y)

y = [2, 2.5, 3, 3.5]


for element in y:
    result = solve_ivp(func, [0, 6], [element], atol = 1e-12, rtol = 1e-9)
    #print('t=',result.t)
    #print(result)
    #print('\ny=',result.y[0])
    plt.plot(result.t, result.y[0], '-')

plt.xlabel('t')
plt.ylabel('y')
plt.legend(['y0 = 2', 'y0 = 2.5', 'y0 = 3', 'y0 = 3.5'])
plt.show()