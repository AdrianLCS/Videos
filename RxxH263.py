import numpy as np
import matplotlib.pyplot as plt

with open('mr_bean_h263_64k.txt') as arquivo:
    vline = arquivo.readlines()

l = []
for i in vline:
    l.append(int(i))

m = 0
var = 0
freq0 = 1 / len(l)
for i in l:
    m = m + i * freq0
for i in l:
    var = var + ((i - m) ** 2) * freq0
desvpad = var ** (1 / 2)

################CORRELAÇAO DE FUNÇÃO#######################
corr = []
tau = []
cont = 0
for i in range(0, 26000, 200):
    corraux = 0
    for j in range(len(l)):
        if j + i < len(l):
            corraux += l[j] * l[j + i]*freq0
    corr.append(corraux)
    tau.append(cont)
    cont += 200
################CORRELAÇAO DE FUNÇÃO#######################


plt.title('Correlação Rxx: mr_bean_h263_64k ')
plt.xlabel('lag')
plt.ylabel('Correlação')
plt.bar(tau, corr, width=110)
plt.show()
