# Jakub Ignatowicz zadanie 6 lista 3
import numpy as np
from scipy import linalg as slin

# tworze wektor n-ow
n = np.array([5, 10, 20])

# petla sluzaca do obliczenia i wyswietlenia normy oraz wskaznika uwarunkowania macierzy Hilberta dla n = [5,10,20]
for i in range(0, 3):
    H = slin.hilbert(n[i])
    print(f"n = {n[i]}\tNorma macierzy Hilberta = {slin.norm(H)}\tWskaznik uwarunkowania macierzy Hilberta = {np.linalg.cond(H)}")
# norma okresla nam "wielkosc" macierzy, wyniki w naszym zadaniu wydaja sie byc poprawne, jednakze wiadomo ze przy coraz wiekszych n blad wyniku bedzie coraz wiekszy
# wskaznik uwarunkowania dla macierzy okresla nam w jakim stopniu blad reprezantacji numerycznej danej macierzy wplywa na obliczenia na niej wykonywane,
# tzn. im wiekszy wyjdzie nam wskaznik uwarunkowania, tym wiekszym bledem obarczone beda wyniki dzialania na takiej macierzy
# jak widac w naszym zadaniu, wskazniki te wychodza bardzo duze (zwlaszcza dla n = 20), co mowi nam o tym ze dzialania na macierzach Hilberta rozwiazywane numerycznie
# beda obarczone nieproporcjonalnie wielkim bledem wyniku