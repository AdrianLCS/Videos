import numpy as np
import matplotlib.pyplot as plt

with open('mr_bean_h263_64k.txt') as arquivo:
    vline = arquivo.readlines()

l = []
for i in vline:
    l.append(int(i))


l2=[]
for i in l:
    if not(i in l2):
        l2.append(i)

hist = np.histogram(l, len(l2))

m1=0
m2=0
var1=0
var2=0
freq = 1/len(l)
cont=0
vezes=0
vezes2=0
for i in hist[1]:
    if i<1200:
        vezes+=hist[0][cont]
        cont+=1
    else:
        vezes2 += hist[0][cont]

for i in range(cont):
    m1 = m1 + hist[0][i]*hist[1][i] * (1/vezes) #quantas vezes apraece x valor
for i in range(cont):
    var1 = var1 + ((hist[1][i] - m1) ** 2) * hist[0][i]*(1/vezes)
for i in range(cont,2077,1):
    m2 = m2 + hist[0][i]*hist[1][i] * (1/vezes2) #quantas vezes apraece x valor
for i in range(cont,2077,1):
    var2 = var2 + ((hist[1][i] - m2) ** 2) * hist[0][i]*(1/vezes2)


print(m1)
print(var1)
print(m2)
print(var2)


print(hist)

m = 0
var = 0



for i in l:
    var = var + ((i - m) ** 2) * freq
g = []
i = 0
h = 100
while i < len(l)-h:
    s = 0
    for j in range(h):
       s += l[i+j]
    g.append(s)
    i += h


desvpad = var ** (1 / 2)


l = np.array(l)
def gausiana1(x):
    return (1/(((np.pi*2*22912.34513766336)**(1/2))))*np.e**((-(x-775.3518451689862)**2)/(2*22912.34513766336))
def gausiana2(x):
    return (1/(((np.pi*2*50800.127292907964)**(1/2))))*np.e**((-(x-1596.3709905409871)**2)/(2*50800.127292907964))

x=np.array(range(-100,10000,20))





#plt.title('Histograma: mr_bean_h263_64k')
plt.xlabel('valor')
plt.ylabel('Frequência')

#plt.hist(l,len(l2), rwidth=0.98, weights=np.ones_like(l) / len(l))
#plt.hist(g, 25)
plt.specgram(l, Fs=40, )
f=gausiana1(x)
f2=gausiana2(x)
#plt.plot(x,f,'r')
#plt.plot(x,f2,'g')

plt.show()
