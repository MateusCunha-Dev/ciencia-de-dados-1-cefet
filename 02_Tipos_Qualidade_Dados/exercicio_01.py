import numpy as np
# Matriz de dados (Data Matrix)
# Colunas:
# 0: ID_Funcionario
# 1: Idade (em anos)
# 2: Codigo_Departamento (0 = RH, 1 = TI, 2 = Vendas)
# 3: Salario (em R$)
dados = np.array([
    [101, 25.0, 1.0,  3000.0],
    [102, 30.0, 0.0,  4500.0],
    [103, np.nan, 1.0, 3200.0],
    [104, 45.0, 2.0, -4000.0],
    [105, 29.0, 0.0,  4100.0],
    [106, 35.0, 1.0,  3600.0],
    [107, 40.0, 2.0, 500000.0],
    [106, 34.0, 1.0,  3600.0],
    [108, 35.0, 1.0,  3600.0],
    [108, 35.0, 1.0,  3600.0]
])

np.set_printoptions(suppress=True, precision=2)


# Exericício 01)
print("--------Exerciício 01---------")
print(
    f"Coluna 0 -> ID_Funcionario = Nominal\n" +
    "Coluna 1 -> Idade = Razão\n"+
    "Coluna 2 -> Codigo_Departamento = Nominal\n"+
    "Coluna 3 -> Salario = Razão\n")


print(f"Cálculo de médias pelo método np.mean(dados, axis=0): {np.mean(dados, axis=0)}")
print(f"Cálculo de médias pelo método np.nanmean(dados, axis=0): {np.nanmean(dados, axis=0)}\n")



# Exercicio 02)
print("--------Exerciício 02 ---------")
media_sem_nan = np.round(np.nanmean(dados[:, 1]), 2)
print(f"Média de idade apenas de registros sem NAN: {media_sem_nan}") # media sem nan

dados_copia = dados.copy() #criando uma cópia para não alterar diretos na base de dados
dados_copia[np.isnan(dados_copia)] = media_sem_nan

dados = dados_copia #base de dados atualizada
print(f"Dados atualizados sem NAN: \n {dados}")



# Exercicio 03)
print("\n--------Exerciício 03 ---------")
salarios_negativos = dados[:,3] < 0
print(f"Selecione todos os valores menores que 0: {dados[(dados < 0)]}\n") #mostra dados negativos
dados[salarios_negativos] = np.abs(dados[(salarios_negativos)]) #corrige para virar em positivo

registros_unicos = np.unique(dados, axis=0) #Apenas corrige duplicados
dados = registros_unicos


# Exercicio 04)
print("--------Exerciício 04 ---------")
teto_salarial = 20000 
coluna_salarios = dados[:,3]
print(f"Registro do funcionário com salário outlier: {dados[coluna_salarios > teto_salarial]}\n")

print(f"Dados atualizados:\n {dados}")