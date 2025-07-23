# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:27:03 2024

@author: pc
"""

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

podaci = np.array([
        [0, 1, -1],
        [1, 0, -1],
        [1, 1, -1],
        [0.5, 0.5, -1],        
        [3, 3 ,1],
        [4, 3, 1],
        [3, 4, 1],
        [3.5, 3.5, 1]
]).astype(float)

crveni = podaci[:, 2]>0
plavi  = podaci[:, 2]<0

fig, (ax1) = plt.subplots(1, 1);
plt.subplots_adjust(wspace=.8);
fig.set_size_inches(10, 4);

ax1.scatter(podaci[crveni,0],podaci[crveni,1], c='r');
ax1.scatter(podaci[plavi,0],podaci[plavi,1], c='b');
plt.grid();
plt.show();

 #y=a1*x1+a2*x2+a3*1

w=np.array([1, 1, 1]);
x=np.array([[x1, x2, 1] for x1 in np.linspace(-2, 5, 20) for x2 in np.linspace(-2, 5, 20)]) ;
y=np.dot(x, w)


class Neuron:
    def forward(self, x,w):
        self.w=w;
        self.x=x;        
        return np.dot(x, w);
    def backward(self, dy):
        dw=dy * self.x;
        dx=dy * self.w;
        return [dw, dx];  


## --- inicijalni parametri ucenja ----    
W=np.array([0.1, 0.1, 0.1]).astype(float)

network=Neuron();
korak_ucenja=0.01;

##---- trening, obucavanje ----------
for epoch in range(5):
    err=0
    for i in range(0, len(podaci)):
        X=podaci[i,0:2];
        X=np.hstack([X, 1.]);
        Y_ocekivano=podaci[i,2];
        
        # forward -- napred
        Y_izracunato=np.sign(network.forward(X,W))

        # backward -- nazad 
        dY = Y_ocekivano - Y_izracunato;
        err += np.abs(dY)
        delta = network.backward(dY);  
        W += korak_ucenja * delta[0]
    print('Epoch={}, Error={}, Model: W={}'.format(epoch,err,W)) 
print(W)

# test i iscrtavanje rezultata testa

xP=np.array([[x1, x2, 1] for x1 in np.linspace(-2, 5, 20) for x2 in np.linspace(-2, 5, 20)]) ;
#print(xP)
yP=network.forward(xP,W)   #samo forward
#

fig, (ax1) = plt.subplots(1, 1);
plt.subplots_adjust(wspace=.8);
fig.set_size_inches(10, 4);

plavi = yP<0
crveni= yP>0

ax1.scatter(xP[plavi,0],xP[plavi,1], alpha=.3, c='b');
ax1.scatter(xP[crveni,0],xP[crveni,1], alpha=.3, c='r');


crveni = podaci[:, 2]>0
plavi  = podaci[:, 2]<0
ax1.scatter(podaci[crveni,0],podaci[crveni,1], c='r');
ax1.scatter(podaci[plavi,0],podaci[plavi,1], c='b');
plt.grid();
plt.show()

##----pojedinacni test
xT = np.array([-2, 1, 0])
y = np.sign(network.forward(xT, W))
print('y='+ str(y))