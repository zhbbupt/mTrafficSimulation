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

class Configure(object):
    mapConf={}
    trafficConf={}
    eNodeBConf={}
    terminalConf={}
    conf_file={}
    conf={}
    def loadConfFile(self,commonConf):
        self.conf_file=loadConfAsDict(commonConf)
        self.mapConf=loadConfAsDict(self.conf_file["map"]["conf_file"])
        self.trafficConf=loadConfAsDict(self.conf_file["traffic"]["conf_file"])
        self.eNodeBConf=loadConfAsDict(self.conf_file["eNodeB"]["conf_file"])
        self.terminalConf=loadConfAsDict(self.conf_file["terminal"]["conf_file"])
    def loadNormalConf(self):
        self.conf["mapConf"]={}
        self.conf["trafficConf"]={}
        self.conf["eNodeBConf"]={}
        self.conf["terminalConf"]={}

        self.conf["mapConf"]["shape_tpye"]=self.mapConf["map"]["shape_tpye"]
        self.conf["mapConf"]["dictance"]=self.mapConf["map"]["dictance"]

        self.conf["trafficConf"]["commonTraffic"]={}
        self.conf["trafficConf"]["commonTraffic"]["density"]=self.trafficConf["commonTraffic"]["density"]

        self.conf["eNodeBConf"]["frequence"]=self.eNodeBConf["eNodeB"]["frequence"]
        self.conf["eNodeBConf"]["transmit_power"]=self.eNodeBConf["eNodeB"]["transmit_power"]
        self.conf["eNodeBConf"]["tti"]=self.eNodeBConf["eNodeB"]["tti"]
        self.conf["eNodeBConf"]["height"]=self.eNodeBConf["eNodeB"]["height"]

        self.conf["terminalConf"]["commonTerminal"]={}
        self.conf["terminalConf"]["commonTerminal"]["height"]=self.terminalConf["commonTerminal"]["height"]
        self.conf["terminalConf"]["commonTerminal"]["rate"]=self.terminalConf["commonTerminal"]["rate"]




    def __init__(self,conmonConf):
        self.loadConfFile(conmonConf)
        self.loadNormalConf()

