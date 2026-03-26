import numpy as np
PATH = "04_Pratica_Pre_Processamento/bases_de_dados_NB04"

np.set_printoptions(suppress=True, precision=2)
imoveis = np.loadtxt(f"{PATH}/nb04_db05_imoveis.csv", delimiter=',')

print("\n-------- exercicio 5.1----------\n")
quarto_0 = imoveis[0]
quarto_1 = imoveis[1]

diff_absoluta = np.abs(quarto_1 - quarto_0)
print(f"Diferença absoluta entre os móveis 1 e 0: \n{diff_absoluta}\n")


print("\n-------- exercicio 5.2----------\n")
coluna_quartos = imoveis[:,0]
coluna_precos = imoveis[:,1]

quartos_padronizados = ((coluna_quartos - np.mean(coluna_quartos))/ np.std(coluna_quartos))
precos_padronizados = ((coluna_precos - np.mean(coluna_precos))/ np.std(coluna_precos))

print(f"Quartos dos imóveis padronizados: \n{quartos_padronizados}\n")
print(f"Preços dos imóveis padronizados: \n{precos_padronizados}\n")


print("\n-------- exercicio 5.3----------\n")
imoveis_copia = np.copy(imoveis)
imoveis_copia[:,0] = quartos_padronizados
imoveis_copia[:,1] = precos_padronizados


quarto_0_padronizado = imoveis_copia[0]
quarto_1_padronizado = imoveis_copia[1]

diff_absoluta_padronizado = np.abs(quarto_1_padronizado - quarto_0_padronizado)
print(f"Diferença absoluta entre os móveis 1 e 0 usando a matriz padronizada: \n{diff_absoluta_padronizado}\n")


print("\n-------- exercicio 5.4----------\n")
media_precos = np.round(np.mean(coluna_precos), 2)
print(media_precos)


print("\n-------- exercicio 5.5----------\n")
mediana_quartos = np.median(imoveis[:,0])
mediana_precos = np.median(imoveis[:,1])

dp_absoluto_quarto = (np.mean(np.abs(imoveis[:,0] - mediana_quartos)))
dp_absoluto_preco = (np.mean(np.abs(imoveis[:,1] - mediana_precos)))

imoveis_final = np.copy(imoveis)
quarto_final = ((coluna_quartos - mediana_quartos))/ dp_absoluto_quarto
preco_final = ((coluna_precos - mediana_precos))/ dp_absoluto_preco
imoveis_final[:,0] = quarto_final
imoveis_final[:,1] = preco_final


print(imoveis_final[:5])

