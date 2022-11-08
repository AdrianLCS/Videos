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
freq0 = 1 / len(lh)

mh = 0
varh = 0
VMQh = 0
for i in lh:
    mh = mh + i * freq0
for i in lh:
    varh = varh + ((i - mh) ** 2) * freq0
desvpadh = varh ** (1 / 2)
for i in lh:
    VMQh = VMQh + i**2 * freq0
print(mh)
print(varh)
print(VMQh)

lm = lm[:len(lh)]
mm = 0
varm = 0
VMQm = 0
for i in lm:
    mm = mm + i * freq0
for i in lm:
    varm = varm + ((i - mm) ** 2) * freq0
desvpadm = varm ** (1 / 2)
for i in lh:
    VMQm = VMQm + i**2 * freq0
print(mm)
print(varm)
print(VMQm)

covariancia = 0
for j in range(len(lh)):
    covariancia += (lm[j] - mm) * (lh[j] - mh) * freq0
print(covariancia)

##############VETORES####################################
VetorMed = np.array([mh, mm])
MatrizVar = np.array([[varh, covariancia], [covariancia, varm]])
print(MatrizVar)
AutoValoreAutoVetor = np.linalg.eig(MatrizVar)
print(AutoValoreAutoVetor) #array de autovalor e matriz com os autovetores
MatrizVarDiagonal = np.array([[AutoValoreAutoVetor[0][0], 0], [0, AutoValoreAutoVetor[0][1]]])
print(MatrizVarDiagonal)
################CORRELAÇAO DE FUNÇÃO#######################
cov = []
tau = []
cont = 0
for i in range(0, 25000, 15):
    covaux = 0
    for j in range(len(lh)):
        if j + i < len(lh):
            covaux += (lm[j]-mm) * (lh[j + i]-mh)*freq0/(desvpadh*desvpadm)
    cov.append(covaux)
    tau.append(cont)
    cont += 15
################CORRELAÇAO DE FUNÇÃO#######################

#plt.title('Coeficiente de Correlação cruzada  ρxy: mr_bean mpeg4 e h263 ')
#plt.xlabel('lag')
#plt.ylabel('Correlação')
#plt.plot(tau, cov)
#plt.show()