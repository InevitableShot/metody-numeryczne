# Jakub Ignatowicz zadanie 3 lista 2
import numpy as np

def func_one(x):
    return np.sqrt(x*x+1)-1

def func_two(x):
    return (x*x)/(np.sqrt(x*x+1)+1)

for n in range(2,400):
    print(f"Dla n = {n}\nWyrażenie 1 = {func_one(2**(-n))}\nWyrażenie 2 = {func_two(2**(-n))}\n")