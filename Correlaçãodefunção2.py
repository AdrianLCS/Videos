import numpy as np
import matplotlib.pyplot as plt

with open('mr_bean_mpeg4_hq.txt') as arquivo:
    vline = arquivo.readlines()
l = []
for i in vline:
    if not i == '\n':
        s = int(i)
        l.append(s)

m = 0
var = 0
freq0 = 1 / len(l)
for i in l:
    m = m + i * freq0
for i in l:
    var = var + ((i - m) ** 2) * freq0
desvpad = var ** (1 / 2)

l2 = []
fatNormalizacao = 0
for i in l:
    fatNormalizacao += i
    if not i in l2:
        l2.append(i)
tamanho = len(l2)

################CORRELAÇAO DE FUNÇÃO#######################
corr = []
tau = []
cont = 0
lnormalizado = list(np.array(l)/fatNormalizacao)
for i in range(0,20000,2000):
    corraux = 0
    for k in range(len(lnormalizado)):
        for j in range(len(lnormalizado)):
            if j + i < len(lnormalizado):
                corraux += lnormalizado[k] * lnormalizado[j + i]
    corr.append(corraux)
    tau.append(cont)
    cont += 2000
################CORRELAÇAO DE FUNÇÃO#######################


plt.title('Correlação: mr_bean_mpeg4_hq.txt')
plt.xlabel('tau')
plt.ylabel('Correlação')
plt.bar(tau, corr,width=1600)
plt.show()
