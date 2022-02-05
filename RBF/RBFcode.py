# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:52:56 2019

@author: Yasna
"""
#سینتکس این سری را رد منزل چک کنید.
#در منزل دیتاست ورودی به الگوریتم ک مین بدهید و سیگما و میو را از کا مین خروجی بگیرید و به شبکه ار بی اف بدهید.
import math
import numpy as np

class RBF:
    def__init__(self,mi,sig)
        self.bias=np.random.uniform(size=(1,1))
        print(self.bias)
        self.w=np.random.uniform(size=(len(mi),1)
        
        def train(Data,Ydesire):
             self.data=Data
             self.yd=Ydesire
             self.yhat=0
             while (self.error>0.1):
                 for k in range(0,len(Data)):         
             
                     for i in range (0,len(mi):
                          self.Gu[i][1]=(1/math.sqrt(2*pi*sig[i][1]))*math.exp((data[k][1]-mi[i][1])**2/(2sig[i][1]**2))
                          self.y[i][1]=self.w[i][1]*self.Gu[i][1]
                          self.yhat[k][1]=self.yhat[k][1]+self.y[i][1]
                
                     self.yhat[k][1]=self.yhat[k][1]+self.bias   
                     self.error=(self.yd[k][1]-self.yhat[k][1])**2
             
            
                     for in range(0,len(mi)):
                          self.w[i][1]=self.w[i][1]+(-self.error)*2*math.exp((data[i][1]-mi[i][1])**2/(2sig[i][1]**2))
                          self.bias=(-self.error*2)+self.bias
                 
                
                 
            
        #ده تا نقطه از سینوس وردی بدم خروجی بگیرم که سینوس رو برام تخمسن بزنه      

        