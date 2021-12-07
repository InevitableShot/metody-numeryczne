# Jakub Ignatowicz zadanie 5 lista 3
import numpy as np


def Gauss(A, b):
    # ilosc wierszy w macierzy A
    n = len(A)
    for k in range(n):                              # petla po wierszach macierzy A
        # szukanie maksymalnej wartosci
        i_max = abs(A[k:, k]).argmax() + k
        if i_max != k:                              # zamiana wierszy jesli warunek jest spelniony
            A[[k, i_max]] = A[[i_max, k]]
            b[[k, i_max]] = b[[i_max, k]]
        for j in range(k+1, n):                   # petla po kolumnach
            f = A[j, k]/A[k, k]                   # wyliczenie wspolczynnika
            A[j, k:] = A[j, k:] - f*A[k, k:]
            b[j] = b[j] - f*b[k]

    x = np.zeros(n)
    for k in range(n-1, -1, -1):
        # wyliczenie x-ow i umieszczenie w wektorze
        x[k] = (b[k] - np.dot(A[k, k+1:], x[k+1:]))/A[k, k]
    return x


# zadanie 1
C = np.array([[-1., 1., -4.],
              [2., 2., 0.],
              [3., 3., 2.]])

D = np.array([[0.], [1.], [0.5]])
print("Zadanie 1")
print(Gauss(C, D))
# funkcja poprawnie obliczyla wyniki

# zadanie 2
print("Zadanie 2")
L = np.array([[1., 0., 0.],
              [3/2, 1., 0.],
              [1/2, 11/13, 1.]])

b = np.array([[1.], [-1.], [2.]])

y = Gauss(L, b)

U = np.array([[2., -3., -1.],
              [0., 13/2, -7/2],
              [0., 0., 32/13]])

print(Gauss(U,y))
# funkcja poprawnie obliczyla wyniki

# zadanie 3
A = np.array([[0., 0., 2., 1., 2.],
              [0., 1., 0., 2., -1.],
              [1., 2., 0., -2., 0.],
              [0., 0., 0., -1., 1.],
              [0., 1., -1., 1., -1.]])
B = np.array([[1.], [1.], [-4.], [-2.], [-1.]])
print("Zadanie 3")
print(Gauss(A, B))
# funkcja poprawnie obliczyla wyniki

# zadanie 4
print("Zadanie 4")
x = np.array([[1., 0., 0., 0., 0.],
              [1., 1., 1., 1., 1.],
              [1., 3., 9., 27., 81.],
              [1., 5., 25., 125., 625.],
              [1., 6., 36., 216., 1296.]])
y = np.array([[-1.], [1.], [3.], [2.], [-2.]])
print(Gauss(x, y))
# funkcja poprawnie obliczyla wyniki
