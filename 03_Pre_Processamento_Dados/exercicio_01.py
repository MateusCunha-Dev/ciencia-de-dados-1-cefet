import numpy as np

np.random.seed(42)

# Simulando 20 clientes. Colunas:
# 0: ID do Cliente
# 1: Idade (em anos)
# 2: Renda Anual (em R$, note que há grande variação)
# 3: Categoria de Fidelidade (0 = Bronze, 1 = Prata, 2 = Ouro)
# 4: Gasto Mensal (em R$)

dados_clientes = np.array([
    [1,  25,   35000, 0,  450],
    [2,  45,  120000, 2, 2100],
    [3,  30,   45000, 1,  800],
    [4,  55,  250000, 2, 4500],
    [5,  22,   28000, 0,  300],
    [6,  34,   60000, 1, 1200],
    [7,  40,   85000, 1, 1500],
    [8,  60,  500000, 2, 8000], # Outlier de renda e gasto!
    [9,  28,   42000, 0,  600],
    [10, 38,   75000, 1, 1400],
    [11, 50,  150000, 2, 3000],
    [12, 26,   32000, 0,  400],
    [13, 33,   58000, 1, 1100],
    [14, 42,   90000, 1, 1600],
    [15, 65,  400000, 2, 7000], # Outlier
    [16, 29,   48000, 0,  750],
    [17, 36,   65000, 1, 1300],
    [18, 48,  130000, 2, 2500],
    [19, 24,   30000, 0,  350],
    [20, 39,   80000, 1, 1450]
], dtype=float)


np.set_printoptions(suppress=True, precision=2)

print("------- Exercício 01 -------")
indices_sorteados = np.random.choice(len(dados_clientes), size=5, replace=False)
print(f"Índices sorteados: {indices_sorteados}\n")
amostra_clientes = dados_clientes[indices_sorteados]
print(f"Cinco clientes sorteados da base de dados: \n{amostra_clientes}\n")



print("------- Exercício 02 -------\n")

renda_anual = dados_clientes[:,2]
renda_log = np.log10(renda_anual)
idades_clientes = dados_clientes[:,1]

media_idades = np.mean(idades_clientes)
dp_clientes = np.std(idades_clientes) 

idades_padronizada = ((idades_clientes - media_idades) / dp_clientes)
print(f"Idades padronizadas (Z-score): \n{idades_padronizada}\n")
dados_clientes[:,1] = idades_padronizada
dados_clientes[:,2] = renda_log



print("------- Exercício 03 -------\n")

gm_clientes = dados_clientes[:,4]

categorias_gasto = np.zeros(len(gm_clientes), dtype=int) 
categorias_gasto[(gm_clientes >= 1000) & (gm_clientes <= 3000)] = 1 
categorias_gasto[gm_clientes > 3000] = 2 
print(f"Nova coluna discretizada: \n{categorias_gasto}\n")
dados_clientes[:,4] = categorias_gasto


print("------- Exercício 04 -------\n")

categorias = dados_clientes[:,3].astype(int)
num_classes = np.max(categorias) + 1
binarizado = np.eye(num_classes)[categorias]

dados_clientes = np.delete(dados_clientes, 3, axis=1)
dados_clientes = np.hstack((dados_clientes, binarizado))


print(f"Dados dos clientes atualizados: \n{dados_clientes}\n")