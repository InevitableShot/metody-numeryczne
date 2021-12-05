# Jakub Ignatowicz zadanie 7 lista 4
import numpy as np

polynomial_coefficients=[1,5+1j,-(8-5j),30-14j,-84]

roots=np.roots(polynomial_coefficients)

print("Pierwiastki funkcji wynosza:")
for i in range(len(roots)):
    print(f'x{i} = {np.round(roots[i])}')

# Pierwiastki wychodza oczywiscie z okreslona dokladnoscia, musimy wiec przyblizyc ze liczby bardzo male sa zerami