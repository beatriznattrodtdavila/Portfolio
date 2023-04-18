import numpy as np
import pandas as pd
import glob
import os

# Criando uma lista com todos os arquivos que possuem extensão .prn no diretório do meu PATH
files_path = "PATH do local onde se encontram os arquivos"
all_files = sorted(glob.glob(os.path.join(files_path,"*.prn"))) # arquivos organizados ordenados

print(all_files)

# Passando por todos os elementos desta lista
# Lendos estes arquivos e fazendo uma seleção neste arquivo lido
# Seleção: Pegando todas as linhas onde a coluna 0 possua valor maior igual a 3.5
# Salvando esta seleção em um novo arquivo
for i in range(0, len(all_files)):
    data = np.loadtxt(all_files[i])
    data = data[data[:, 0] >= 3.5]
    print(data)
    np.savetxt('/home/fsc/Documents/6_LiF_6 MeV_Cu/Spec' + str(i + 1) + '-LiF-60s.txt', data, delimiter = ' ')