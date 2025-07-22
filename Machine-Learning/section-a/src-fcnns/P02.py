# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:27:03 2024

@author: pc
"""

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

x = np.array([1,2,3,4,5,6,7]).astype(np.float32)
y = np.array([2.1, 3.9, 5.7, 8.01, 10.1, 11.9, 13.7]).astype(np.float32)
#y = np.array([2,3,4,5,6,7,8,9]).astype(np.float32)

class Neuron:
    def forward(self, w,x):
        self.w=w;
        self.x=x;
        y=w*x;
        return y;
    def backward(self, dy):
        dx=self.w*dy;
        dw=self.x*dy;
        return [dw, dx];   
    
class Neuron0:
    def forward(self, w0,g):
        self.g=g;
        self.w0=w0;
        y=w0+g;
        return y;
    def backward(self, dy):
        dg=dy;
        dw0=dy;
        return [dw0, dg];    

def grafik(x, y, y_Izracunato):
    x_osa=(0, 10);
    fig, (ax1) = plt.subplots(1, 1);
    plt.subplots_adjust(wspace=.8);
    fig.set_size_inches(10, 5);
    ax1.scatter(x, y, alpha=.7, c='b');
    ax1.plot(x_osa, [y_Izracunato(X) for X in x_osa], "g", alpha=.7, c='r');
    plt.grid();
    plt.show();
  
# --- inicijalni parametri ucenja ----    
w=0.1;
w0=0.1;
neuronX=Neuron();
neuron0=Neuron0();
korak_ucenja=0.01;

#grafik(x, y, lambda x: neuron.forward(w,x)); 

#---- trening, obucabanje ----------
for epoch in range(5):
    for i in range(len(x)):
        X=x[i];
        Y_ocekivano=y[i];
        # forward -- napred
        
        g=neuronX.forward(w, X)
        Y_izracunato=neuron0.forward(w0,g)
        # backward -- nazad   
        dY=Y_ocekivano - Y_izracunato;
        [dw0, dg]=neuron0.backward(dY)
        [dw, dx]=neuronX.backward(dg);
        w += korak_ucenja*dw;
        w0 += korak_ucenja*dw0;
       
        grafik(x, y, lambda x: neuron0.forward(w0,neuronX.forward(w,x))); 
        print('Epoch={} Model: w0={}, w={}'.format(epoch,w0,w))  
        input(" ");
        
#---- trening, obucabanje ----------

       
grafik(x, y, lambda x: neuron0.forward(w0,neuronX.forward(w,x)));          
print('Epoch={} Model: w0={}, w={}'.format(epoch,w0,w))     
