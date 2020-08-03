# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:59:47 2020

@author: user
"""

KG=input("你的體重kg")
M=input("你的身高")
M = float(M)
BMI=float(KG)/float(M)*float(M)
if float(BMI)<18.5:
    print("體重不足")
elif float(BMI)<24:
    print("正常")
elif float(BMI)<27:
    print("過重")
elif float(BMI)<30:
    print("輕度肥胖")
elif float(BMI)<36:
    print("中度肥胖")
else:
    print("重度肥胖")