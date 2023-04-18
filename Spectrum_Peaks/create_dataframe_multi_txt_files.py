import os
import glob
import pandas as pd
import numpy as np
 
# Criando um dataframe a partir de vaŕios arquivos .txt


# Criando uma lista com todos os arquivos no diretório que possuam extensão .txt
files_path = "/home/fsc/Documents/Beatriz_Nattrodt_Davila/Mestrado/2_LiF_6MeV_Cu_electron_gun"
all_files = glob.glob(os.path.join(files_path,"*egun.txt"))

#print(all_files)

li=[]
i = 0
columns_names = ["Count"]

# Lendo todos os nomes dos arquivos contidos no diretório e jogando eles no read_csv para criar um dataframe e adicionando este dataframe a uma lista (lista de dataframes)
for filename in all_files:
	df = pd.read_csv(filename, delimiter = ' ')
	li.append(df)

print(li)

# Concatenando todos os dataframes da lista em 1 único dataframe
frame = pd.concat(li, axis=1, join = 'inner', ignore_index = True)

# Excluindo todas as colunas pares diferentes de 0 do dataframe
for col in frame.columns:
        if i !=0:
                resto = i % 2
                if resto == 0 :
                            del frame[col]

        i = i + 1


col_list = list(frame)
col_list.remove(0)
frame["Sum"] = frame[col_list].sum(axis=1)
   
print(frame)

# Salvando dataframe
frame.to_csv('Concat_DataFrame.dat', header = None,  sep = '\t')