import numpy as np

def eq1(x):
    return np.sqrt(np.float32((x**4)+4))-2

def eq2(x):
    return (x**4)/(np.sqrt(np.float32((x**4)+4))+2)

for n in range(2,32):
    x = 2 ** (-n)
    #x = n
    print("x =", x)
    print("Wzor 1:", eq1(x))
    print("Wzor 2:", eq2(x), "\n")