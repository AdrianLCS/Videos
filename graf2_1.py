import numpy as np
import matplotlib.pyplot as plt

with open('mr_bean_mpeg4_hq.txt') as arquivo:
    vline = arquivo.readlines()
l = []
for i in vline:
    if not i == '\n':
        s = int(i)
        l.append(s)

l2 = []
for i in l:
    if not i in l2:
        l2.append(i)
tamanho = len(l2)

m=0
var=0
freq=1/len(l)
for i in l:
    m = m+i*freq
print(m)

for i in l:
    var = var+((i-m) ** 2) * freq
print(var)
desvpad=var**(1/2)
print(desvpad)

#print(l)
#print(l2)

x=np.array(range(len(l)))

plt.title('sinal de video mr_bean_mpeg4_hq')
plt.xlabel('ordem')
plt.ylabel('valor')
plt.plot(x,l, 'g')
plt.show()


