# -*- coding: utf-8 -*-
'''
Created on 2016-06-05 21:53
summary: my math tools 
author: zhbbupt
'''
import math
PI=3.14
def max(a,b):
    if a>b:
        return a
    else:
        return b 
def min(a,b):
    if a<b:
        return a
    else:
        return b 
def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
