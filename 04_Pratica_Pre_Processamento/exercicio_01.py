import numpy as np
PATH = "04_Pratica_Pre_Processamento/bases_de_dados_NB04"

np.set_printoptions(suppress=True, precision=2)

print("\n------- Exercício 1.1) -------\n")
vendas = np.loadtxt(f"{PATH}/nb04_db01_vendas.csv", delimiter=',')
coluna_id = vendas[:,0]
coluna_vendas = vendas[:,2]
ids = np.unique(coluna_id)

resultado = []

for i in ids:
    vendas_loja = coluna_vendas[coluna_id == i]
    media_vendas = np.mean(vendas_loja)
    resultado.append(media_vendas)

vendas_mensais = np.array(resultado)
print(f"Médias de vendas mensais (Lojas 1 a 5): {vendas_mensais}\n")



print("\n------- Exercício 1.2) -------\n")
coef_variabilidade_diario = np.round(np.std(coluna_vendas) / np.mean(coluna_vendas),4)
coef_variabilidade_mensal = np.round(np.std(vendas_mensais) / np.mean(vendas_mensais),4)

print(f"CV diario: {coef_variabilidade_diario}")
print(f"CV vendas mensais: {coef_variabilidade_mensal}\n")


print("\n------- Exercício 1.3) -------\n")
indice_vendas = np.random.choice(len(vendas), size=15, replace=False)
amostra_vendas = vendas[indice_vendas]
print(f"Amostra de 15 vendas: \n{amostra_vendas}\n")



print("\n------- Exercício 1.4) -------\n")
ids_selecionados_amostra = amostra_vendas[:,0] - 1
count = np.bincount(ids_selecionados_amostra.astype(int)) 
print(f"Quantidade de vendas na amostra da [Loja 1, Loja 2, Loja 3, Loja 4, Loja 5]: {count}\n")
print("Está desbalanceado. A aleatoriedade 'cega' não foi justa")



print("\n------- Exercício 1.5) -------\n")
pedacos_da_amostra = []

for loja in ids:
    dados_loja = vendas[vendas[:,0] == loja]
    indices_sorteados = np.random.choice(len(dados_loja), size=3, replace=False)
    pedacos_da_amostra.append(dados_loja[indices_sorteados])

amostra_final_estratificada = np.vstack(pedacos_da_amostra)
np.random.shuffle(amostra_final_estratificada)
print(f"Amostragem final estratificada (15 itens balanceados e embaralhados): \n{amostra_final_estratificada}\n")

