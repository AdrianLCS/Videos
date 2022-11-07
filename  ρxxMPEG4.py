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

################CORRELAÇAO DE FUNÇÃO#######################
cov = []
tau = []
cont = 0
for i in range(0,400, 1):
    covaux = 0
    for j in range(len(l)):
        if j + i < len(l):
            covaux += (l[j]-m) * (l[j + i]-m)*freq0/var
    cov.append(covaux)
    tau.append(cont)
    cont += 1
################CORRELAÇAO DE FUNÇÃO#######################


plt.title('Coeficiente de Correlação  ρxx: mr_bean_mpeg4_hq.txt')
plt.xlabel('lag')
plt.ylabel('Correlação')
plt.plot(tau, cov)
plt.show()
