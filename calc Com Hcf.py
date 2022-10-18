import os
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pasta = os.getcwd()
lista = os.listdir(pasta)
origem = lista[4]

im = Image.open(origem)
im = im.convert('RGB')

    

r=[]
g=[]
b=[]
w = im.size[0]
h = im.size[1]



r,g,b=im.split()
rhist=r.histogram()
ghist=g.histogram()
bhist=b.histogram()
'''
#################HISTOGRAMA###################
im = np.array(im)
for i in range(h):
    for j in range(w):
        r.append(im[i][j][0])
        g.append(im[i][j][1])
        b.append(im[i][j][2])

x=[range(0,255)]
rhist=[]
ghist=[]
bhist=[]
for i in x:
    rhist.append(r.count(i)/len(r))
    ghist.append(g.count(i)/len(g))
    bhist.append(b.count(i)/len(b))
#################HISTOGRAMA###################
'''
hcfr=np.fft.rfft(rhist)
hcfg=np.fft.rfft(ghist)
hcfb=np.fft.rfft(bhist)

print(len(hcfr))
coms=0
comi=0
for i in range(int(len(hcfr)/2)):
    coms+=i*abs(hcfr[i])
    comi+=abs(hcfr[i])
comr=coms/comi

coms=0
comi=0
for i in range(int(len(hcfr)/2)):
    coms+=i*abs(hcfg[i])
    comi+=abs(hcfg[i])
comg=coms/comi

coms=0
comi=0
for i in range(int(len(hcfr)/2)):
    coms+=i*abs(hcfb[i])
    comi+=abs(hcfb[i])
comb=coms/comi

print(comr)
print(comg)
print(comb)