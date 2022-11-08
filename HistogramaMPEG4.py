import numpy as np
import matplotlib.pyplot as plt

with open('mr_bean_mpeg4_hq.txt') as arquivo:
    vline = arquivo.readlines()
l = []
for i in vline:
    if not i == '\n':
        s = int(i)
        l.append(s)
l2=[]
for i in l:
    if not(i in l2):
        l2.append(i)

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
    return (1/(((np.pi*2)**(1/2))*desvpad))*np.e**((-(x-m)**2)/(2*var))


x=np.array(range(-2000,15000,2000))
#plt.subplot(2, 1, 2)
plt.title('Histograma: mr_bean_mpeg4_hq')
plt.xlabel('valor')
plt.ylabel('Frequência')

plt.hist(l, len(l2), rwidth=0.95,weights=np.ones_like(l)/len(l))
plt.xticks(x)
t=np.array(range(-2000,15000,10))
f=gausiana(t)
#plt.specgram(l, Fs=40)
plt.plot(t,f,'r')
plt.show()