# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:41:10 2022

@author: tavakoli
"""


class Fraction:
    def __init__(self,n1,d1,n2,d2):
        self.num1=n1
        self.den1=d1
        self.num2=n2
        self.den2=d2
    def add(self):
        frac1=(self.num1*self.den2)/(self.den1*self.den2)
        
        frac2=(self.num2*self.den1)/(self.den2*self.den1)
        add_r=(frac1+frac2)
        print(add_r)
        
    def sub(self):
        frac1=(self.num1*self.den2)/(self.den1*self.den2)
        
        frac2=(self.num2*self.den1)/(self.den2*self.den1)
        sub_r=(frac1-frac2)
        print(sub_r)
    def mul(self):
        frac1=(self.num1*self.num2)
        
        frac2=(self.den1*self.den2)
        mul_r=(frac1,'/',frac2)
        print(mul_r) 
    def div(self):
        frac1=(self.num1*self.den2)
        
        frac2=(self.num2*self.den1)
        div_r=(frac1,"/",frac2)
        print(div_r) 
    
test=Fraction (2,2,1,3)            
test.add()
test.sub()
test.mul()
test.div()