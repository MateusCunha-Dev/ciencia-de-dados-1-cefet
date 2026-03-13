import numpy as np

vendas = np.array([
    [120, 135, 150, 160, 170, 200, 210], # Loja 1
    [80,  90,  95,  100, 110, 120, 130], # Loja 2
    [200, 210, 220, 230, 250, 260, 300], # Loja 3
    [60,  65,  70,  80,  85,  90,  95],  # Loja 4
    [150, 160, 170, 180, 190, 210, 230]  # Loja 5
])

totais_lojas = np.sum(vendas, axis=1)
totais_dias = np.sum(vendas, axis=0)
totais_desvios_lojas = np.std(vendas, axis=1)

# Exercício A)
print(f"Quantas vendas totais foram realizadas na semana? {np.sum(vendas)}")

# Exercício B) 
print(f"Qual foi a média de vendas considerando todas as lojas e dias? {np.mean(vendas):.2f}")

# Exercício C)
print(f"Qual foi o maior valor de vendas registrado? {np.max(vendas)}")

# Exercício D)
print(f"Qual foi o menor valor de vendas registrado? {np.min(vendas)}")

# Exercício E)
print(f"Média de vendas de cada loja na semana: {np.round(np.mean(vendas, axis=1),2)}")

# Exercício F)
print(f"Qual loja teve o maior total de vendas? {np.argmax(totais_lojas) + 1}")

# Exercício G)
print(f"Qual loja apresentou maior variabilidade nas vendas (desvio padrão)? {np.argmax(totais_desvios_lojas) + 1}")

# Exercício H)
print(f"Qual foi o dia com maior número total de vendas? {np.argmax(totais_dias) + 1}")

# Exercício I)
print(f"Qual foi a média de vendas por dia considerando todas as lojas? {np.mean(vendas, axis=0)}")






