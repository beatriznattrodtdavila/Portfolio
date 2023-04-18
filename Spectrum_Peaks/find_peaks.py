import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import pandas as pd


# Encontrando os picos do espectro e salvando as coordenadas desses picos em um arquivo
# Plotando e salvando uma imagem do espectro com os picos destacados

li6 = 6.015123
li7 = 7.016004
f = 18.998403
tof = 0.1305
C = 2.592
delta_M1 = 0.01
delta_M2 = 0.05
delta_M3 = 0.1
delta_M4 = 1

data = np.loadtxt("Concat_DataFrame.dat") #lendo arquivos de dados
x1 = data[:,1] #Selecionando coluna - Time
y1 = data[:,43] #Selecionando coluna - Sum_specs
h1 = np.std(y1)/10 #Definindo altura minima para achar máximos
d1 = 500 #distancia entre máximos






peaks = scipy.signal.find_peaks(y1, height = h1, width = 0.1, prominence = 650, distance = 100)
x1_max = x1[peaks[0]] #Lista da posição dos picos
y1_max = peaks[1]['peak_heights'] #Lista das alturas dos picos

picos = zip(x1_max, y1_max)


######## Plot ##########
plt.plot(x1,y1,"-",label="data")
plt.plot(x1_max,y1_max,".",label="máximos")
plt.axhline(y=h1,color="r",label="std(y1)/3")

plt.xlabel("Time of Flight(\u03bcs)")
plt.ylabel("Count")
plt.xticks(np.arange(0, 50, 5))
plt.title("Peaks for LiF 6MeV Cu Electron Gun All Add")

plt.legend()
plt.grid()
#plt.savefig('Peaks.png')
plt.show()


with open('picos.txt', 'w') as my_file:
    for (x1_max,y1_max) in picos:
        my_file.write("{0}\t{1}\n".format(x1_max,y1_max))
print('File created')