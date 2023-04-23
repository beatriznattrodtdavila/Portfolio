import pandas as pd


# Criando uma função para criar as URLs necessárias
def build_url(gene):
    return "https://raw.githubusercontent.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20" + gene + ".csv"


# Criando uma lista com as URLs
url_list = []
for i in range(10, 21):
    for j in range(1,3):
        url_list.append(build_url(str(i) + str(j)))

# Criando uma lista de dataframes, onde cada elemento da lista é o dataframe referente a url lida
dataframe_list = []
for i in range(0,(len(url_list)-1)):
    data = pd.read_csv(url_list[i])
    dataframe_list.append(data)

# Concatenando todos os dataframes da lista em apenas um único dataset
emprestimos_biblioteca = pd.concat(dataframe_list, join = 'inner', ignore_index = True)

# Verificando a existencia de dados duplicados
quantidade_antes = emprestimos_biblioteca.shape[0]
emprestimos_biblioteca = emprestimos_biblioteca.drop_duplicates()
quantidade_depois = emprestimos_biblioteca.shape[0]


if(quantidade_antes == quantidade_depois):
    print("Não há dados duplicados no nosso dataset")
    print("Temos: " + str(quantidade_antes.shape[0]) + "dados no nosso dataset")
else:
    print("Há dados duplicados no nosso dataset e eles foram excluidos\n")
    print("Dados anteriores: " + str(quantidade_antes) + ".\nDados após exclusão: " + str(quantidade_depois) + ".\n")
    print("Diferença do número de dados após a exclusão de duplicatas: " + str(quantidade_antes - quantidade_depois))



# Criando um novo dataset
dados_exemplares = pd.read_parquet('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet')


# Unindo ambos os datasets
emprestimos = emprestimos_biblioteca.merge(dados_exemplares)



# Criando uma nova coluna
CDU_lista = []

for i in emprestimos.localizacao:
    if (i < 100):
        CDU_lista.append("Generalidade. Ciência e Conhecimento")
    elif(i >= 100 and i < 200):
        CDU_lista.append("Filosofia e Psicologia")
    elif(i >= 200 and i < 300):
        CDU_lista.append("Religião")
    elif(i >= 300 and i < 400):
        CDU_lista.append("Ciências Sociais")
    elif(i >= 400 and i < 500):
        CDU_lista.append(" - ")
    elif(i >= 500 and i < 600):
        CDU_lista.append("Matemática e Ciência Naturais")
    elif(i >= 600 and i< 700):
        CDU_lista.append("Ciência Aplicadas")
    elif(i >= 700 and i < 800):
        CDU_lista.append("Belas Artes")
    elif(i >= 800 and i < 900):
        CDU_lista.append("Linguagem. Lingua. Linguistica")
    else:
        CDU_lista.append("Geografia. Biografia. História")

emprestimos["CDU"] = CDU_lista


# Excluindo coluna
emprestimos.drop("registro_sistema", axis = 1, inplace = True)


# Mudando tipo de uma coluna
emprestimos["matricula_ou_siape"] = emprestimos["matricula_ou_siape"].astype(str)

print(emprestimos.dtypes)

# Criando um arquivo .csv com o dataframe final
#emprestimos.to_csv("Emprestimos.csv", sep = "\t", index = False)
