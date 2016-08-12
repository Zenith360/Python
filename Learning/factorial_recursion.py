# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:29:23 2016

@author: james
"""

def factorial(x):
    if x == 1:
        return 1;
    print(x)
    return x * factorial(x - 1)

print()

    
print(factorial(100));