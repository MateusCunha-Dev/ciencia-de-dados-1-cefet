import numpy as np
PATH = "04_Pratica_Pre_Processamento/bases_de_dados_NB04"

np.set_printoptions(suppress=True, precision=2)
visualizacoes = np.loadtxt(f"{PATH}/nb04_db04_visualizacoes.csv", delimiter=',')

print("\n------- Exercício 4.1) -------\n")
video99 = visualizacoes[98]
video98 = visualizacoes[97]
video97 = visualizacoes[96]
video96 = visualizacoes[95]

diff_absoluta_A = np.abs(video99 - video98)
diff_absoluta_B = np.abs(video97 - video96)
print(f"Diferença abslouta de visualizações entre os vídeos 99 e 98: \n{np.round(diff_absoluta_A, 2)} views\n")
print(f"Diferença abslouta de visualizações entre os vídeos 97 e 96: \n{np.round(diff_absoluta_B, 2)} views\n")
print("Em números absolutos, o par de vídeos com maior diferença é o 99 e 98\n")


print("\n------- Exercício 4.2) -------\n")
visualizacao_log = np.log10(visualizacoes)
print(visualizacao_log)



print("\n------- Exercício 4.3) -------\n")
video99_log = visualizacao_log[98]
video98_log = visualizacao_log[97]
video97_log = visualizacao_log[96]
video96_log = visualizacao_log[95]

diff_absoluta_A_log = np.abs(video99_log - video98_log)
diff_absoluta_B_log = np.abs(video97_log - video96_log)
print(f"Diferença abslouta de visualizações entre os vídeos 99 e 98: \n{np.round(diff_absoluta_A_log, 2)}\n")
print(f"Diferença abslouta de visualizações entre os vídeos 97 e 96: \n{np.round(diff_absoluta_B_log, 2)}\n")

print("Na primeira base de dados a diferença entre visualizaçõs\n" \
      "eram enormes, podendo se assemelhar com números outliers.\n" \
      "Na base dados nova, o logaritmo comprime amplitudes massivas,\n" \
      "sendo assim, impede que os algoritmos de Machine Learning\n" \
      "tratem esses vídeos virais como outliers\n")