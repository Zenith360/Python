# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:51:15 2016

@author: james
"""

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for i in start_list:
    square_list.append(i ** 2);
square_list.sort();
print(square_list)