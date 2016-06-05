# -*- coding: utf-8 -*-
'''
Created on 2016-06-05 22:15
summary: load configure file
author: zhbbupt
'''


import Utils.mathTools 
from Utils.configTools import loadConfAsDict
import pdb  
def loadConf(commonConf):
    conf=loadConfAsDict(commonConf)
    mapConf=loadConfAsDict(conf["map"]["conf_file"])
    trafficConf=loadConfAsDict(conf["traffic"]["conf_file"])
    eNodeBConf=loadConfAsDict(conf["eNodeB"]["conf_file"])

