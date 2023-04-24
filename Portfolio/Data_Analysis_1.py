import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
df_emprestimos_biblioteca = pd.concat(dataframe_list, join = 'inner', ignore_index = True)

# Verificando a existencia de dados duplicados
quantidade_antes = df_emprestimos_biblioteca.shape[0]
df_emprestimos_biblioteca = df_emprestimos_biblioteca.drop_duplicates()
quantidade_depois = df_emprestimos_biblioteca.shape[0]


if(quantidade_antes == quantidade_depois):
    print("Não há dados duplicados no nosso dataset")
    print("Temos: " + str(quantidade_antes.shape[0]) + "dados no nosso dataset")
else:
    print("Há dados duplicados no nosso dataset e eles foram excluidos\n")
    print("Dados anteriores: " + str(quantidade_antes) + ".\nDados após exclusão: " + str(quantidade_depois) + ".\n")
    print("Diferença do número de dados após a exclusão de duplicatas: " + str(quantidade_antes - quantidade_depois))



# Criando um novo dataset
df_dados_exemplares = pd.read_parquet('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet')


# Unindo ambos os datasets
df_emprestimos = df_emprestimos_biblioteca.merge(df_dados_exemplares)



# Criando uma nova coluna
CDU_lista = []

for i in df_emprestimos.localizacao:
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

df_emprestimos["CDU"] = CDU_lista


# Excluindo coluna
df_emprestimos.drop("registro_sistema", axis = 1, inplace = True)


# Mudando tipo de uma coluna
df_emprestimos["matricula_ou_siape"] = df_emprestimos["matricula_ou_siape"].astype(str)

# Criando um arquivo .csv com o dataframe final
#df_emprestimos.to_csv("Emprestimos.csv", sep = "\t", index = False)






# Respondendo algumas perguntas

# 1. Quantidade total de exemplares emprestados
df_emprestimos["id_emprestimo"].value_counts() # o mesmo id_emprestimos aparece mais de uma vez
df_emprestimos.loc[df_emprestimos["id_emprestimo"] == 2422542] # cada linha em que o mesmo id_emprestimo aparece é um exemplar diferente emprestado 

qtd_exemplares_emprestados = len(df_emprestimos["id_emprestimo"].index) # A quantidade de exemplares emprestados é a quantidade de linhas do dataframe

# 2. Quantidade total de emprestimos realizados
qtd_emprestimos_realizados = len(df_emprestimos["id_emprestimo"].drop_duplicates().index)

# 3. Quantidade total de exemplares emprestados por ano
df_emprestimos.dtypes # datas não estao no tipo data, necessita transformação
df_emprestimos.loc[:, ["data_renovacao", "data_emprestimo", "data_devolucao"]] = df_emprestimos.loc[:, ["data_renovacao", "data_emprestimo", "data_devolucao"]].apply(pd.to_datetime)


# Criando um dataframe apenas da quantidade de exemplares emprestados pelo ano de emprestimo
#df_exemplares_emprestados= df_emprestimos[["data_emprestimo"]]
#df_exemplares_emprestados= df_exemplares_emprestados.value_counts()
#df_exemplares_emprestados= df_exemplares_emprestados.to_frame().reset_index()
#df_exemplares_emprestados.columns = ["data", "quantidade"]
#df_exemplares_emprestados_ano = df_exemplares_emprestados.groupby(by = df_exemplares_emprestados.data.dt.year).sum()


df_exemplares_emprestados_ano = df_emprestimos.loc[:, "data_emprestimo"].dt.year.value_counts().to_frame()
df_exemplares_emprestados_ano.columns = ["Quantidade"]
df_exemplares_emprestados_ano.index.name = "Ano"

# Gráfico
#sns.lineplot(data = df_exemplares_emprestados_ano, x = "Ano", y = "Quantidade")
#plt.title("Quantidade de Exemplares Emprestados ao Longo dos Anos")
#plt.grid()
#plt.show()


# 4. Quantidade total de exemplares emprestados de acordoo com os meses do ano
#df_exemplares_emprestados= df_emprestimos[["data_emprestimo"]]
#df_exemplares_emprestados= df_exemplares_emprestados.value_counts()
#df_exemplares_emprestados= df_exemplares_emprestados.to_frame().reset_index()
#df_exemplares_emprestados.columns = ["data", "quantidade"]
#df_exemplares_emprestados_mes = df_exemplares_emprestados.groupby(by = df_exemplares_emprestados.data.dt.month).sum()
#df_exemplares_emprestados_mes = df_exemplares_emprestados_mes.sort_index(ascending = True)


df_exemplares_emprestados_mes = df_emprestimos.loc[:, "data_emprestimo"].dt.month.value_counts().to_frame()
df_exemplares_emprestados_mes.columns = ["Quantidade"]
df_exemplares_emprestados_mes.index.name = "Meses"
df_exemplares_emprestados_mes = df_exemplares_emprestados_mes.sort_index(ascending = True)

meses_do_ano = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4:  "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

df_exemplares_emprestados_mes.index = df_exemplares_emprestados_mes.index.map(meses_do_ano)


#Gráfico
#sns.lineplot(data = df_exemplares_emprestados_mes, x = "Meses", y = "Quantidade")
#plt.title("Quantidade de Exemplares Emprestados ao Longo dos Meses do Ano")
#plt.grid()
#plt.show()

# 5. Quantidade total de exemplares emprestados de acordo com as horas do dia
#df_exemplares_emprestados= df_emprestimos[["data_emprestimo"]]
#df_exemplares_emprestados= df_exemplares_emprestados.value_counts()
#df_exemplares_emprestados= df_exemplares_emprestados.to_frame().reset_index()
#df_exemplares_emprestados.columns = ["data", "quantidade"]
#df_exemplares_emprestados_hora = df_exemplares_emprestados.groupby(by = df_exemplares_emprestados.data.dt.hour).sum()
#df_exemplares_emprestados_hora = df_exemplares_emprestados_hora.reset_index()
#df_exemplares_emprestados_hora.columns = ["Hora","Quantidade"]
#df_exemplares_emprestados_hora = df_exemplares_emprestados_hora.sort_index(ascending = True)


df_exemplares_emprestados_hora = df_emprestimos.loc[:, "data_emprestimo"].dt.hour.value_counts().to_frame().reset_index()
df_exemplares_emprestados_hora.columns = ["Hora","Quantidade"]
df_exemplares_emprestados_hora = df_exemplares_emprestados_hora.sort_index(ascending = True)

#sns.barplot(data = df_exemplares_emprestados_hora, x = "Hora", y = "Quantidade")
#plt.title("Quantidade de Exemplares Emprestados ao Longo das Horas do Dia")
#plt.grid()
#plt.show()
