import os
import numpy as np
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
im.resize((int(w/2),int(h/2))).save(origem[0:str(origem).rfind(".")] + "v2.png")
im2f=im.resize((int(w/2),int(h/2)))

im = np.array(im)
im2f=np.array(im2f)
for i in range(int(h/2)):
    for j in range(int(w/2)):
        im2r=0
        im2g=0
        im2b=0
        for k in range(2):
            for z in range(2):
                im2r+=(1/4)*im[2*i+k][2*j+z][0]
                im2g+=(1/4)*im[2*i+k][2*j+z][1]
                im2b+=(1/4)*im[2*i+k][2*j+z][2]
        im2f[i][j][0]=im2r
        im2f[i][j][1]=im2g
        im2f[i][j][2]=im2b

im2f=Image.fromarray(im2f)
im2f.save(origem[0:str(origem).rfind(".")] + "v2.png")
       
                
            