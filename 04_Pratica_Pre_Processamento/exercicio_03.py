import numpy as np
PATH = "04_Pratica_Pre_Processamento/bases_de_dados_NB04"

np.set_printoptions(suppress=True, precision=2)
objetos = np.loadtxt(f"{PATH}/nb04_db03_objetos.csv", delimiter=',')

print("\n------- Exercício 3.1) -------\n")
id = objetos[:,0]
massa = objetos[:,1]
volume = objetos[:,2]

densidade = massa / volume
print(f"Densidade (Apenas 10 primeiras): \n{densidade[:10]}\n")

print("\n------- Exercício 3.2) -------\n")
objetos = np.column_stack((objetos, densidade))
print(f"Empilhando Densidade (Apenas 10 primeiras): \n{objetos[:10]}\n")




print("\n------- Exercício 3.3) e 3.4) -------\n")
categorias_densidade = np.zeros(len(densidade), dtype=int)
categorias_densidade[(densidade >= 5.0) & (densidade <= 10.0)] = 1 
categorias_densidade[densidade > 10.0] = 2

objetos = np.column_stack((objetos, categorias_densidade))

print(f"Discretização da coluna de Densidade e empilhando Categoria (Apenas 10 primeiras): \n{objetos[:10]}\n")



print("\n------- Exercício 3.5) -------\n")

categorias = objetos[:,4].astype(int)
num_classes = np.max(categorias) + 1
binarizado = np.eye(num_classes)[categorias]

objetos = np.delete(objetos, 4, axis=1)
objetos = np.hstack((objetos, binarizado))
print(f"Base de dados de objetos atualizada: \n{objetos}\n")