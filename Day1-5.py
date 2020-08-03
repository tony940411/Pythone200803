# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:29:07 2020

@author: user
"""

x=input("你的成績")
x=int(x)
if x>=0 and x<=100:
    if x>=90 and x<=100:
        print("A")
    elif x>=80 and x<90:
            print("B")
    elif x>=70 and x<80:
            print("C")
    elif x>=60 and x<70:
            print("D")
    else:
            print("E")
    