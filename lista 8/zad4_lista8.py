# Jakub Ignatowicz zadanie 4 lista 8
import numpy as np
from scipy.sparse.linalg import eigsh
from scipy.sparse import diags
import matplotlib.pyplot as plt

# Dane z zadania
lam = 0.2   # lambda
a = 4.6
m = 100     # Aby uzyskac wykres dla wartosci m = 1000, nalezy zmienic wartosc w tym miejscu

# Tworze siatke rownoodleglych punktow za pomoca wzoru z zadania
h = 2*a/m

# Tworze liste elementow na diagonali, tych elementow jest m-1 (wzor z zadania)
d = np.fromfunction(lambda i : (1.0 / (h**2)) + (((-a+(i+1)*h) ** 2)/2.0) + (lam * (-a+(i+1)*h)**4) , (m-1,), dtype = float)

# Tworze liste elementow nad/pod diagonala, tych elementow jest m-2 (wzor z zadania)
g = (-1.0/(2.0 * (h ** 2))) * np.ones(m-2)

# Konwertuje wszystkie elementy na liste list 
data = [d.tolist(), g.tolist(), g.tolist()]

# Ustawiam pozycje aby umiescic powyzsze dane w macierzy
positions=[0, 1, -1]

# Tworze macierz rzadka (sparse matrix) za pomocą funkcji diags(), przy okazji wybieram format csc, 
# ktory to preferowany jest przez funckje eigsh() z ustawiona opcja sigma
H = diags(data, positions, (m-1, m-1)).tocsc()

# Otrzymuje wartosci wlasne oraz wektory wlasne za pomoca funkcji eigsh, obliczam 4 wartości własne ustawiajac k=4,
# lezace najblizej sigma = 0 , uzycie opcji sigma wymaga ustawienia which = 'LM', w przeciwnym wypadku otrzymamy error
values, vectors = eigsh(H, k = 4, sigma = 0.0, which = 'LM')

print('Wartości własne (najmniejsze energie) =')
for value in values:
    print(value)

# Tworze okno z 4 podwykresami, po 1 wykresie na kazda wartosc najmniejszych energii wlasnych
figure, axs = plt.subplots(4)

# Ustawiam wielkosc wykresu
figure.set_size_inches(20, 12)

# Ustawiam zakres x-ow
xx=np.arange(h-a,a-h+1e-12,h)

# Tworze petle dla czterech wartosci wlasnych
for i in range(4):
    # Stosuje normowanie danych
    nv = 1 / np.sqrt((h * (vectors[:,i] ** 2)).sum())  
    
    # Rysowanie wykresu
    axs[i].plot(xx, nv * vectors[:,i], label=f"E = {values[i]}")

    # Ustawienia wykresu
    axs[i].set_xlabel("x")
    axs[i].set_ylabel("y")
    axs[i].legend(loc = 'upper right')
    plt.title('Funkcje falowe', loc = 'center')

plt.show()

