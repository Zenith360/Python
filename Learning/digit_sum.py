# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:07:01 2016

@author: james
"""

def digit_sum(n):
    sumDigits = 0;    
    for c in str(n):
        sumDigits += int(c);
    print(sumDigits);
    return sumDigits;
digit_sum(1234);