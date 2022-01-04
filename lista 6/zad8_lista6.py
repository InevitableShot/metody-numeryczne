# Jakub Ignatowicz zadanie 8 lista 6
import numpy as np
from scipy.integrate import dblquad

# Definiuje funkcje z zadania
def func(x, y): 
    return np.sin(np.pi*x)*np.sin(np.pi*(y-x))

def lower(x):
    return 0

def upper(x):
    return x

# Obliczam wartosc za pomoca wolfram alpha
# https://www.wolframalpha.com/input/?i=int+from+0+to+1+of+%28%28int+from+0+to+x+of+%28%28sin%28pi*x%29*sin%28pi*%28y-x%29%29%29dy%29%29dx%29
value = -2/(np.pi*np.pi)

result, error = dblquad(func, 1, 0, lower, upper)
print(f"Obliczona wartosc calki = {result}\t blad = {np.abs(value - result)}")

# Otrzymany wynik jest zgodny z tym obliczonym przez wolfram alpha, jest on oczywiscie obarczony niewielkim bledem numerycznym