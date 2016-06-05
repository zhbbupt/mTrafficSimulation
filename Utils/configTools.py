# -*- coding:utf-8 -*-
'''
created on : 5/29/2016 6:15:42 PM
'''
import ConfigParser
import logging
from Utils.mathTools import *
import pdb 
#本模块由于提取配置文件
def getValue(input):
    if isInt(input):
        return int(input)
    if isFloat(input):
        return float(input)
    return str(input)
def loadConfAsDict(file):
    config={}
    cf = ConfigParser.ConfigParser()
    cf.read(file)
    for sec in cf.sections():
        config[sec]={}
        for opt in cf.options(sec):
            config[sec][opt]=getValue(cf.get(sec,opt))
    return config

