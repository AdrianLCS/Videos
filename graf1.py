import numpy as np
import matplotlib.pyplot as plt

with open('mr_bean_h263_64k.txt') as arquivo:
    vline = arquivo.readlines()

l = []
for i in vline:
    l.append(int(i))

m = 0
var = 0
freq = 1 / len(l)

for i in l:
    m = m + i * freq
print(m)

for i in l:
    var = var + ((i - m) ** 2) * freq

print(var)

desvpad = var ** (1 / 2)

print(desvpad)
l2 = []
for i in l:
    if not i in l2:
        l2.append(i)

tamanho = len(l2)

freq = []
cont = 0
for i in l2:
    freq.append(l.count(l2[cont]))
    cont += 1

corr = []
corraux=0
tau = []
cont = 0
for i in range(len(l2)):
    for j in range(len(l2)):
        if j+i < len(l2):
            corraux += l2[j]*l2[j+i]
    corr.append(corraux)
    tau.append(cont)
    cont += 1
l = np.array(l)
l2 = np.array(l2)

plt.title(
    'Histograma: mr_bean_h263_64k \n Média: 1115.5629311012997 \n Variância: 197099.38507710805 \n Desvio padrão: 443.9587650639506')
plt.xlabel('valor')
plt.ylabel('Frequência Relativa')
plt.hist(l, 100, rwidth=0.95, weights=np.ones_like(l) / len(l))
plt.show()
