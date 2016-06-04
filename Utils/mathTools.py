# -*- coding:utf-8 -*-
'''
created on : 4/29/2016 6:44:38 PM
fileName   : mathTools.py
author     : zhbbupt
TODO       : 
'''
import math
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