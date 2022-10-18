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
x=np.array(range(len(l)))
plt.title('Sinal de video mr_bean_h263_64k')
plt.xlabel('nr de ordem')
plt.ylabel('valor')
plt.plot(x, l)
plt.show()