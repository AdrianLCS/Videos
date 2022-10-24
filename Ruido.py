import numpy as np
import random
import matplotlib.pyplot as plt

r = []
for i in range(1000):
    r.append(int(random.gauss(0, 2)))

m = 0
var = 0
freq0 = 1 / len(r)
for i in r:
    m = m + i * freq0
for i in r:
    var = var + ((i - m) ** 2) * freq0
desvpad = var ** (1 / 2)

################CORRELAÇAO DE FUNÇÃO#######################
corr = []
tau = []
cont = 0
for i in range(0, 1000, 10):
    corraux = 0
    for j in range(len(r)):
        if j + i < len(r):
            corraux += (r[j]-m) * (r[j + i]-m)*freq0/var
    corr.append(corraux)
    tau.append(cont)
    cont += 10
################CORRELAÇAO DE FUNÇÃO#######################


plt.title('Coeficiente de Correlação Pxx: Ruido')
plt.xlabel('lag')
plt.ylabel('Correlação')
plt.bar(tau, corr, width=9)
plt.show()
