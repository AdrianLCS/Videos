import numpy as np
import matplotlib.pyplot as plt

with open('mr_bean_mpeg4_hq.txt') as arquivo:
    vline = arquivo.readlines()
lm = []
for i in vline:
    if not i == '\n':
        s = int(i)
        lm.append(s)


with open('mr_bean_h263_64k.txt') as arquivo:
    vline = arquivo.readlines()

lh = []
for i in vline:
    lh.append(int(i))

mh = 0
varh = 0
freq0 = 1 / len(lh)
for i in lh:
    mh = mh + i * freq0
for i in lh:
    varh = varh + ((i - mh) ** 2) * freq0
desvpadh = varh ** (1 / 2)

lm = lm[:len(lh)]
mm = 0
varm = 0

for i in lm:
    mm = mm + i * freq0
for i in lm:
    varm = varm + ((i - mm) ** 2) * freq0

desvpadm = varm ** (1 / 2)


################CORRELAÇAO DE FUNÇÃO#######################
cov = []
tau = []
cont = 0
for i in range(0, 400, 1):
    covaux = 0
    for j in range(len(lh)):
        if j + i < len(lh):
            covaux += (lm[j]) * (lh[j + i])*freq0
    cov.append(covaux)
    tau.append(cont)
    cont += 1
################CORRELAÇAO DE FUNÇÃO#######################

plt.title('Correlação cruzada  Rxy: mr_bean mpeg4 e h263 ')
plt.xlabel('lag')
plt.ylabel('Correlação')
#plt.bar(tau, cov, width=170)
plt.plot(tau, cov)
plt.show()