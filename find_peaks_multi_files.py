# Encontrando os picos de varios espectros de uma vez e salvando as coordenadas desses picos em um arquivo para cada espectro
# Plotando e salvando uma imagem do espectro com os picos destacados

import glob
import os
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.signal

 
li6 = 6.015123
li7 = 7.016004
f = 18.998403
tof = 0.1305
C = 2.592
delta_M1 = 0.01
delta_M2 = 0.05
delta_M3 = 0.1
delta_M4 = 1
 
 
all_files = sorted(glob.glob("/home/ubuntu/Documents/Dissertation/Emissão_de_matéria_em_Cristais_Iônicos _Calculo_Tempo_de_Voo_de_Ions_Secundarios/1_LiF_6_MeV_Cu/Spec*.txt"))

print(all_files)


for i in range(0, len(all_files)):
    frame = pd.read_csv(all_files[i], delimiter = ' ', header = None)
    x1 = frame.iloc[:,0].values
    y1 = frame.iloc[:,1].values
    h1 = np.std(y1)/10
    peaks = scipy.signal.find_peaks(y1, height = h1, width = 0.001, prominence = 6.0, distance = 1000)
    x1_max = x1[peaks[0]] #Lista da posição dos picos
    y1_max = peaks[1]['peak_heights'] #Lista das alturas dos picos


    
    picos = zip(x1_max, y1_max)

    plt.plot(x1,y1,"-",label="data")
    plt.plot(x1_max,y1_max,".",label="máximos")
    plt.axhline(y=h1,color="r",label="std(y1)/3")

    plt.xlabel("Time of Flight(\u03bcs)")
    plt.ylabel("Count")
    plt.title("Peaks for LiF 6MeV Cu Electron Gun All Add")

    plt.legend()
    plt.grid()
    plt.savefig('Peaks' + str(i + 1) + '.png')
    plt.show()
    
    with open('picos' + str(i+1) + '.txt', 'w') as my_file:
        for (x1_max,y1_max) in picos:
            my_file.write("{0}\t{1}\n".format(x1_max,y1_max))
    print('File created')