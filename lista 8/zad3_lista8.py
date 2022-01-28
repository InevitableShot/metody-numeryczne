# Jakub Ignatowicz zadanie 3 lista 8
import numpy as np
from scipy.sparse.linalg import eigsh

# Dana z zadania
n = [10, 100]   # Lista zawierajaca wielkosci macierzy (n x n)

# Petla po kazdej zadanej wielkosci macierzy
for element in n:
    print(f"Dla macierzy o wielkosci n = {element}:\n")
    
    # Tworze macierz za pomoca funkcji np.diag, ktora pozwala na operowanie na diagonalach macierzy i ich tworzenie
    H = np.diag(-1 * np.ones(element-1), k = -1) + np.diag(2 * np.ones(element)) + np.diag(-1 * np.ones(element - 1), k=1)
    
    # Otrzymuje wartosci wlasne oraz wektory wlasne za pomoca funkcji eigsh, "SM" odpowiada za wybranie najmniejszych wartosci
    values, vectors = eigsh(H, 3, which="SM")
    for i in range(3):
        print(f"Dla {i+1} wartosci:\n wartosc wlasna = {values[i]}\n\nwektor wlasny = \n{vectors[:, i]}")
        print(f"\n")