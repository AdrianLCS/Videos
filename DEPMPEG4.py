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
corr = []
tau = []
cont = 0
for i in range(0, 4000, 1):
    corraux = 0
    for j in range(len(l)):
        if j + i < len(l):
            corraux += l[j] * l[j + i]*freq0
    corr.append(corraux)
    tau.append(cont)
    cont += 1
################CORRELAÇAO DE FUNÇÃO#######################

fft=abs(np.fft.rfft(corr))
x=range(len(fft))
x=np.array(x)
x=x*40/4000
plt.title('Correlação Rxx: mr_bean_mpeg4_hq.txt')
plt.xlabel('lag')
plt.ylabel('Correlação')
#plt.bar(tau, corr, width= 800)
#plt.plot(tau, corr)
plt.plot(x, fft)
plt.show()
