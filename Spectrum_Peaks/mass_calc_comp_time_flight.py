# Calculando a massa de um íon secundário a partir do seu tempo de voo
# O tempo de voo é proveniente do valor x do pico do espectro - peaks.py

# Comparando esta massa com as massas de uma tabela criada (dfc)
# Passando uma lista com possiveis diferenças entre as massas
# Salvando em um arquivo a massa da tabela, a massa calculada, a diferença utilizada e quanto de LiF 6, LiF 7 e Fluor foram usados para encontrar o valor da massa tabelada


import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import pandas as pd


li6 = 6.015123
li7 = 7.016004
f = 18.998403
tof = 0.1305
C = 2.592
ldelta_M = [0.01, 0.05, 0.10, 1.00]
delta_M1 = 0.01


data = np.loadtxt("picos.txt") #lendo arquivos de dados
x1_max = data[:,0] #Selecionando coluna altura picos
y1_max = data[:,1] #Selecionando coluna posição picos


df = pd.DataFrame(list(zip(y1_max,x1_max)), columns = ["Altura Picos", "Posição Picos"])
df['Massa ToF'] = ((df['Posição Picos']-tof)/C)**2 #calculo massa tof
#print(df)
#df.to_csv('Massa calculada a partir do tempo de voo.txt', sep = '\t')






Comparação = np.loadtxt("Li6_Li7_F.txt") #lendo arquivos de dados


dfc = pd.DataFrame(Comparação, columns = ["Li6", "Li7"]) #criando dataframe
dfc['Fluor'] = dfc['Li6'] + dfc['Li7'] - 1 #criando coluna a partir de colunas existentes
dfc['Massa Tabela'] = dfc['Li6']*li6 + dfc['Li7']*li7 + dfc['Fluor']*f #criando coluna a partir de colunas existentes
dfc['Tempo de Voo'] = (dfc['Massa Tabela']**(0.5))*C-tof #criando uma coluna de tempo de voo atraves das outras colunas existentes
#print(dfc)
#dfc.to_csv('Tempo de voo massa calculada da quantidade de Li6, Li7 e Fluor.txt', sep = '\t')


#with open('Massas Calculadas.txt', 'w') as f:
#        for k in ldelta_M:
#                for i in range(0, len(df['Massa ToF'])):
#                        massa_tof = df['Massa ToF'][i]
#                        for j in range(0, len(dfc['Massa Tabela'])):
#                                massa_tabela = dfc['Massa Tabela'][j]
#                                if((massa_tabela - k < massa_tof) and (massa_tabela + k > massa_tof)):
#                                        print('Para delta_M = ', k, '\nMassa ToF: ', massa_tof, '\nMassa Tabela: ', massa_tabela, '\nLi6: ', dfc['Li6'][j], '\nLi7: ', dfc['Li7'][j], '\nFluor: ', dfc['Fluor'][j], '\n \n', file = f)


with open('Massas Calculadas_no_text.txt', 'w') as f:
        for k in ldelta_M:
                for i in range(0, len(df['Massa ToF'])):
                        massa_tof = df['Massa ToF'][i]
                        for j in range(0, len(dfc['Massa Tabela'])):
                                massa_tabela = dfc['Massa Tabela'][j]
                                if((massa_tabela - k < massa_tof) and (massa_tabela + k > massa_tof)):
                                        print(k, '\t', massa_tof, '\t', massa_tabela, '\t', dfc['Li6'][j], '\t', dfc['Li7'][j], '\t', dfc['Fluor'][j], '\n', file = f)
