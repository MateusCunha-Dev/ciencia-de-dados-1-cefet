import numpy as np

np.random.seed(42)

# Exercício A) 
a = np.arange(101)
print(f"\n Um array com os números de 0 a 100 (Tamanho: {a.size}):\n{a}\n")

# Exercício B) 
b = np.full((5,5), 7)
print(f"Uma matriz 5x5 preenchida com o valor 7 (Shape: {b.shape}):\n{b}\n")


# Exercício C) 
c = np.linspace(0, 10, 50)
print(f"Um array com 50 valores igualmente espaçados entre 0 e 10 (Tamanho: {c.size}):\n{c}\n")


# Exercício D) 
d = np.random.rand(3,3)
print(f"Uma matriz 3x3 aleatória com valores entre 0 e 1 (Shape: {d.shape}): \n{d}\n")