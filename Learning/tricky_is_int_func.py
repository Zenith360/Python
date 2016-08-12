# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:13:25 2016

@author: james
"""

def is_int(x):
    if round(x) - x == 0:
        return True;
    else:
        return False;
is_int(4);