import numpy as np
import matplotlib.pyplot as plt

with open('mr_bean_h263_64k.txt') as arquivo:
    vline = arquivo.readlines()
l=[]
for i in vline:
    l.append(int(i))
m = 0
var = 0
freq=1/len(l)

for i in l:
    m = m+i*freq
print(m)

for i in l:
    var = var+((i-m) ** 2) * freq
print(var)
desvpad=var**(1/2)
print(desvpad)
l2 = []
for i in l:
    if not i in l2:
        l2.append(i)
tamanho = len(l2)



plt.title('Histograma: mr_bean_h263_64k \n Média: 1115.5629311012997 \n Variância: 197099.38507710805 \n Desvio padrão: 443.9587650639506')
plt.xlabel('valor')
plt.ylabel('Frequência Absoluta')
plt.hist(l,tamanho)
plt.show()