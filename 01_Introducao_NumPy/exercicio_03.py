import numpy as np

dados = np.array([12, 45, 23, 67, 34, 89, 15, 56, 78, 90])

# Exercicío A)
print(f"Selecione todos os valores maiores que 50: {dados[(dados > 50)]}")

# Exercicío B)
print(f"Calcule a média apenas dos valores entre 20 e 70: {np.mean(dados[(dados >= 20) & (dados <= 70)])}")

# Exercicío C)
dados_copia = dados.copy()
dados_copia[dados_copia % 2 != 0] = -1
print(f"Substitua todos os valores ímpares por -1: {dados_copia}")

# Exercicío D)
print(f"Extraia os 5 primeiros e os 3 últimos elementos:  {dados[:5]} ----- {dados[-3:]} ")

# Exercicío E)
print(f"Imprima o array ordenado:  {np.sort(dados)} ")

