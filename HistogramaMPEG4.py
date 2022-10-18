import numpy as np
import matplotlib.pyplot as plt

with open('mr_bean_mpeg4_hq.txt') as arquivo:
    vline = arquivo.readlines()
l = []
for i in vline:
    if not i == '\n':
        s = int(i)
        l.append(s)

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

def gausiana(x):
    return (1/(((np.pi*2)**(1/2))*1790.9000112647193))*np.e**((-(x-2911.7464432891047)**2)/(2*3207322.8503479715))


x=np.array(range(-2000,15000,2000))
#plt.subplot(2, 1, 2)
plt.title('Histograma: mr_bean_mpeg4_hq \n Média: 2911.7464432891047 \n Variância: 3207322.8503479715 \n Desvio padrão: 1790.9000112647193')
plt.xlabel('valor')
plt.ylabel('Frequência relativa')
plt.hist(l, 100,rwidth=0.95,weights=np.ones_like(l)/len(l))
plt.xticks(x)
t=np.array(range(-2000,15000,10))
f=gausiana(t)

#plt.plot(t,f,'r')
plt.show()