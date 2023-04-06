import pandas as pd
import numpy as np


Li6 = [0,1,2,3,4,5,6,7,8,9,10]
Li7 = [0,1,2,3,4,5,6,7,8,9,10]

# Criando um arquivo .txt com 2 colunas percorrendo a lista Li6 para todos os valores da lista Li7
with open('Li6_Li7_F.txt', 'w') as f:
    for i in Li6:
        for j in Li7:
            print(i,j, file = f)