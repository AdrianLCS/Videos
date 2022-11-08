import numpy as np
import matplotlib.pyplot as plt
import numpy.fft
import pylab

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
for i in range(0, 2000, 1):
    corraux = 0
    for j in range(len(l)):
        if j + i < len(l):
            corraux += l[j] * l[j + i]*freq0
    corr.append(corraux)
    tau.append(cont)
    cont += 1
corr=np.array(corr)
fft=abs(np.fft.rfft(corr))
################CORRELAÇAO DE FUNÇÃO#######################
fft=20*np.log10(fft)
x = range(len(fft))
x = np.array(x)
x = x*40/2000
plt.title('DEP mr_bean_h263_64k ')
plt.xlabel('Freqência')
plt.ylabel('Potência')
#plt.bar(tau, corr, width=0.9)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(x, fft, lw=2)

ax.set_xscale('log')
pylab.xlabel('Freqência')
pylab.title('DEP mr_bean_h263_64k ')
pylab.xlabel('Freqência')
pylab.show()