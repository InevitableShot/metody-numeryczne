# Jakub Ignatowicz zadanie 3 lista 2
import numpy as np

# Funkcja zwraca wartości dla pierwszego wyrażenia
def func_one(x):
    return np.sqrt(x*x+1)-1

# Funkcja zwraca wartości dla drugiego wyrażenia
def func_two(x):
    return (x*x)/(np.sqrt(x*x+1)+1)

for n in range(2,25):
    print(f"Dla n = {n}\nWyrażenie 1 = {func_one(2**(-n))}\nWyrażenie 2 = {func_two(2**(-n))}\n")

# Drugie wyrażenie daje dokładniejsze wyniki, kiedy porównamy je z Wolframem Alpha
# Co więcej pierwsze wyrażenie dla n = 26 i więcej zaczyna być zerem, co nie jest prawidłowym wynikiem
# natomiast wyrażenie drugie nawet dla większych n nadal podaje poprawne wyniki, oczywiście w granicy błędu