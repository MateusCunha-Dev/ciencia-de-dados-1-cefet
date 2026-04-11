import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

PATH = "05_pandas/bases_de_dados_NB05/nb05_db01_vendas_eletronicos.csv"

print("\n\n")
print("="*60)

print("Exercício 01 ---- carregamento e inspeção da base de dados")
df_vendas = pd.read_csv(PATH) 
df_clean = df_vendas.copy()
print("Visão dos dados originais:\n")
print(df_vendas)
print("\n")
print("Dados originais com NaN nos atributos 'qualidade' e 'bateria_horas'. Textos em 'categoria' e 'tensão' despadronizados.\n")


print("\n")
print("="*60)

print("Exercício 02 ---- Pré-processando, realizando limpeza e tratamento de nulos.\n")
df_clean['categoria'] = df_clean['categoria'].str.replace('celular', 'Smartphone')
df_clean['categoria'] = df_clean['categoria'].str.replace('smartphone', 'Smartphone')
df_clean['categoria'] = df_clean['categoria'].str.replace('notebook', 'Notebook')
df_clean['categoria'] = df_clean['categoria'].str.replace('tablet', 'Tablet')

df_clean['tensao'] = df_clean['tensao'].str.replace('127/220', 'bivolt')
df_clean['tensao'] = df_clean['tensao'].str.replace('127V/220V', 'bivolt')


mediana_bateria = df_clean['bateria_horas'].median()
df_clean['bateria_horas'] = df_clean['bateria_horas'].fillna(mediana_bateria)

moda_qualidade = df_clean['qualidade'].mode()[0]
df_clean['qualidade'] = df_clean['qualidade'].fillna(moda_qualidade)

print(df_clean[['produto', 'qualidade', 'bateria_horas']])

df_clean = df_clean.drop('tensao', axis=1)


df_clean['score_tecnologia'] = (
    df_clean['tem_5g'] + 
    df_clean['tem_touchscreen'] + 
    df_clean['tem_caneta'] + 
    df_clean['tem_leitor_iris'] + 
    df_clean['tem_nfc'] 
)

print("\nUso de moda()[0] e mediana() para substituir os NaN de 'qualidade' e 'bateria_horas' respectivamente. Textos padronizados")
print("\nRemoção da coluna 'tensão' por variância zero. Criação da coluna 'score_tecnologia'")


print("\n")
print("="*60)

print("Exercício 03 ---- Normalização (Min-Max) e Padronização (Z-score)\n")


mapeamento_qualidade = {"ruim": 0, "regular": 1, "boa": 2, "ótima": 3}
df_clean['qualidade_num'] = df_clean['qualidade'].map(mapeamento_qualidade)

min_bateria = df_clean['bateria_horas'].min()
max_bateria = df_clean['bateria_horas'].max()
df_clean['bateria_horas_norm'] = (df_clean['bateria_horas'] - min_bateria) / (max_bateria - min_bateria)

min_tela = df_clean['tela_polegadas'].min()
max_tela = df_clean['tela_polegadas'].max()
df_clean['tela_polegadas_norm'] = (df_clean['tela_polegadas'] - min_tela) / (max_tela - min_tela)

min_qualidade = df_clean['qualidade_num'].min()
max_qualidade = df_clean['qualidade_num'].max()
df_clean['qualidade_norm'] = (df_clean['qualidade_num'] - min_qualidade) / (max_qualidade - min_qualidade)

media_preco = df_clean['preco_reais'].mean()
desvio_preco = df_clean['preco_reais'].std()
df_clean['preco_reais_z_score'] = (df_clean['preco_reais'] - media_preco) / desvio_preco

colunas_finais = ['produto', 'categoria', 'score_tecnologia', 'bateria_horas_norm', 'tela_polegadas_norm', 'qualidade_norm', 'preco_reais_z_score']
print(df_clean[colunas_finais])


print("\n--- 3C. Quando usar Z-Score vs Normalização Min-Max? ---")
print("Deve-se escolher o Z-Score quando identificar um possível outlier na base de dados. " 
      "Se usarmos a normalização Min-Max, o outlier estica o valor 'max', fazendo com que " 
      "todos os dados normais fiquem esmagados/achatados próximos de zero.")

print("\n--- 3D. Por que a 'Categoria' não pode ser normalizada? ---")
print("Porque 'Qualidade' é um atributo Ordinal, ou seja, existe uma hierarquia lógica e matemática "
      "(ótima > boa > regular > ruim) que nos permite mapear pesos e normalizar. " 
      "Já a 'Categoria' (Smartphone, Notebook) é um atributo Nominal. Não existe ordem de grandeza " 
      "entre eles. Se tentássemos dar peso 1 para celular e 2 para notebook, o algoritmo assumiria " 
      "erroneamente que um notebook 'vale o dobro', o que destruiria a análise matemática.")

print("\n")
print("="*60)

print("Exercício 04 ---- Previsão Estratégica\n")

print("1. PRODUTO MAIS VENDIDO (CURTO PRAZO): O Smartphone E possui o melhor Custo-Benefício. " 
      "Ele tem o melhor score de tecnologia (4), nota máxima normalizada em bateria e qualidade, " 
      "além de ter o segundo menor preço da base.\n"
      "2. OFERTAS BLACK FRIDAY: \n"
      "   - Notebook G: Por ter um valor altíssimo (Z-score muito acima da média), é o melhor "
      "candidato para um grande desconto em dinheiro bruto, atraindo o público premium.\n"
      "   - Smartphone F (e Tablet C): Como possuem qualidade baixa e score tecnológico fraco, "
      "tendem a encalhar. Uma promoção agressiva na Black Friday é ideal para esvaziar esse estoque.")
print("\n")
