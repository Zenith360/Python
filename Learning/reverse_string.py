# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:45:29 2016

@author: james
"""
"""Revreses Stuff"""
def reverse(text):
    rev_list = [];
    foo_list = [];
    for i in text:
        rev_list.append(i)
    dev = len(rev_list);
    while dev > 0:
        if(dev != 0):
            f = rev_list[dev - 1];
            foo_list.append(f)
            dev -= 1; 
    x = "".join(foo_list);
    print(x)
    return x;
reverse("asdf");