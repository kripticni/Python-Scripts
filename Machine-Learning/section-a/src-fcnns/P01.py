# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 08:33:35 2024

@author: pc
"""

import numpy as np  #import library for manipulation with arrays and matrices
import matplotlib.pyplot as plt #import library for plot 
#%matplotlib inline

x = np.array([1,2,3,4,5,6,7,8]).astype(np.float32)   # define training dataset
y = np.array([2.1, 3.9, 5.7, 8.01, 10.1, 11.9, 13.7, 15.2]).astype(np.float32)  # define real outputs fro training dataset examples
#y = np.array([2,3,4,5,6,7,8,9]).astype(np.int32)  
    
# define Neuron class
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
    
def grafik(x, y, yIzracunato):
    x_osa=(0, 10);
    fig, (ax1) = plt.subplots(1, 1);
    plt.subplots_adjust(wspace=.8);
    fig.set_size_inches(10, 10);
    ax1.scatter(x, y, alpha=.7, c='b');
    ax1.plot(x_osa, [yIzracunato(X) for X in x_osa], "g", alpha=.7, c='r');
    plt.grid();
    plt.show();
  
# --- inicijalni parametri ucenja ----    
w=0.2;
neuron=Neuron();
korak_ucenja=0.01;

grafik(x, y, lambda x: neuron.forward(w,x)); 


for epoch in range(3):
    for i in range(len(x)):
        X=x[i];
        Y_ocekivano=y[i];
        Y_izracunato=neuron.forward(w,X);
        dY=Y_ocekivano - Y_izracunato;
        [dw, dx]=neuron.backward(dY);
        w += korak_ucenja*dw;
        print('Epoch={} Model: w={}'.format(epoch,w))       
        grafik(x, y, lambda x: neuron.forward(w,x));  
        print("unesi nesto")
        input(" "); 

        
#---- trening, obucabanje ----------

print('Epoch={} Model: w={}'.format(epoch,w))         
grafik(x, y, lambda x: neuron.forward(w,x));  
print('w=' + str(neuron.w))


     
    
