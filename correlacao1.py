import numpy as np
import matplotlib.pyplot as plt

with open('mr_bean_h263_64k.txt') as arquivo:
    vline = arquivo.readlines()

l = []
for i in vline:
    l.append(int(i))

l2 = []
fatNormalizacao = 0

for i in l:
    if not i in l2:
        l2.append(i)
tamanho = len(l2)

freqrel = []
cont = 0
for i in l2:
    freqrel.append(l.count(l2[cont])/len(l))
    cont += 1

################CORRELAÇAO DE HISTOGRAMA#######################
corrH = []
tauH = []
contH = 0

for i in range(0, 2000, 100):
    corrauxH = 0
    for k in range(len(l2)):
        for j in range(len(l2)):
            if j + i < len(l2):
                corrauxH += l2[k]*freqrel[k] * l2[j+i]*freqrel[j+i]

    corrH.append(corrauxH)
    tauH.append(contH)
    contH += 100

################CORRELAÇAO DE HISTOGRAMA#######################
l = np.array(l)
l2 = np.array(l2)

plt.title('Correlação: mr_bean_h263_64k ')
plt.xlabel('tau')
plt.ylabel('Correlação')
plt.bar(tauH, corrH, width=80)
plt.show()
