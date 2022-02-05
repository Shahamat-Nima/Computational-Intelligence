# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:26:27 2019

@author: Yasna
"""

import math
import numpy as np

class hopfield:
    def __init__(self,W,V1):
        self.W =W
        self.V1 = V1
        def sign(V):
          for i in range(0,len(V)):
              if (V[i] < 0):
                  V[i]=-1
              if (V[i]>=0):
                  V[i]=1
          return (V)
          #  self.counter=0
        d=1
        while d==1:
            self.V2 = (self.V1 @ self.W)
            self.V0=sign(self.V2)
            d=0
            for i in range (0,3):  
                if (self.V0[i] != V1[i] ):   
                    self.V1[i] = self.V0[i] 
                    d=1
                    break;
             #   print(self.V0)
               
            
    
    
    
    
    
    
    
    
    
    
   
x1=np.array([1,1,0,0])
x1=x1*2
x1=x1-1
w=(np.transpose(x1)*x1)
print(w)
    
    
    
    
    
    
#W=np.array([[0,0,1,-1],[1,0,1,-1],[1,1,0,-1],[-1,-1,-1,0]])برای قسمت دوم دبلیو رو میسازیم از روی خود الگو و اگر بفرستیم به هاپفیلد باید نشان دهید بردار الگو همان یاست که از روی دبیلو ساختیم .
#x1=np.array([1,1,1,1])
print()   
r=hopfield(W,x1)    
