import numpy as np
PATH = "04_Pratica_Pre_Processamento/bases_de_dados_NB04"

np.set_printoptions(suppress=True, precision=2)
dados = np.loadtxt(f"{PATH}/nb04_db02_dados.csv", delimiter=',')

print("\n------- Exercício 2.1) -------\n")

matriz_correlacao = np.corrcoef(dados, rowvar=False)
print(f"Matriz de correlação: \n{matriz_correlacao}\n")


print("\n------- Exercício 2.2) -------\n")
print(
    "Coluna 1 e 3 correlação = 1\n" \
    "Coluna 2 e 4 correlação = -0.99\n")


print("\n------- Exercício 2.3) -------\n")

dados_filtrados = np.delete(dados, [3,4], axis=1)
print(f"Dados filtrados: \n{dados_filtrados[:10]}\n")


print("\n------- Exercício 2.4) -------\n")

X_c = dados_filtrados - np.mean(dados_filtrados, axis=0)
U, S, Vt = np.linalg.svd(X_c, full_matrices=False)

k = 2
V_k = Vt[:k, :].T
X_reduzido = np.dot(X_c, V_k)

print(f"Amostra projetada:\n{X_reduzido[:10]}\n")
