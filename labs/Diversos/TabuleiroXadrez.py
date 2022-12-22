# Tabuleiro de Xadrez com Python
'''
Instalar o pacotes
pip install numpy && matplotlib
'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

tabuleiro = np.title([1,0],[8,4])

for i in range(tabuleiro.shape[0]):
    tabuleiro[i] = np.roll(tabuleiro[i], i%2)

mapa_de_cores = ListedColormap(['#779556', '#ebecd0'])
plt.matshow(tabuleiro, cmap=mapa_de_cores)
plt.xticks([])
plt.yticks([])
plt.show()
