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
cov = []
tau = []
cont = 0
for i in range(0, 200, 1):
    covaux = 0
    for j in range(len(l)):
        if j + i < len(l):
            covaux += (l[j]-m) * (l[j + i]-m)*freq0/var
    cov.append(covaux)
    tau.append(cont)
    cont += 1
################CORRELAÇAO DE FUNÇÃO#######################


plt.title('Coeficiente de Correlação  ρxx: mr_bean_h263_64k ')
plt.xlabel('lag')
plt.ylabel('Correlação')
#plt.bar(tau, cov, width=30)
plt.plot(tau, cov)
plt.show()
