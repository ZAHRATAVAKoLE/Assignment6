# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 23:35:41 2022

@author: TAVAKOLI
"""

class complex :

    def __init__(self, real=None, image=None):
        self.r = real
        self.i = image
        


    def sub(self, other):
        result=complex()
        result.r= self.r - other.r
        result.i= self.i - other.i
        return result


    def sum(self, other):
        result=complex()
        result.r= self.r + other.r
        result.i= self.i + other.i
        return result



    def mul(self, other):
        result=complex()
        result.r= self.r * other.r - self.i * other.i
        result.i= self.r * other.i - self.i * other.r
        return result


    def show(self):
        return str(self.r )+'+('+str(self.i) +')i'

real1=int(input('enter your complex number1 real: '))
image1=int(input('enter  your complex number2 image: '))


real2=int(input('enter your complex number2 real: '))
image2=int(input('enter your complex number2 image: '))

C1 = complex(real1,image1)
C2 = complex(real2,image2)
print('sum:',(C1.sum(C2)).show())
print('SUB:',(C1.sub(C2)).show())
print('mul:',(C1.mul(C2)).show())