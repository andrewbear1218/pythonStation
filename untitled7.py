# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:13:11 2024

@author: user
"""

total=0
for i in range(2,21):
    if i % 2 == 0:
        print(i,end=",")
    if i %5 ==0:
        total += i
print()
print("5的倍數和:",total)

    
        