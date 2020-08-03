# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:23:11 2020

@author: user
"""

M=input("數學成績")
E=input("英文成績")
M=int(M)
E=int(E)
if M>=90 and E>=90:
    print("有獎勵")
elif M>=60 and E<60:
    print("再加油")
elif E<60 and M<60:
    print("要懲罰")
else:
    print("再加油")
    




