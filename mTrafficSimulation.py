# -*- coding:utf-8 -*-
'''
Created on : 4/28/2016 1:48:58 PM
fileName   : mTrafficSimulation.py
author     : zhbbupt
TODO       : 
'''
from TrafficModule.basicTraffic import  basicTraffic
import PropagationModule.propagationModel as pro
import logging
import logging.config
import ConfigParser
import string, os, sys
import pdb 
from Utils.configTools import loadConfAsDict
from loadConf import *
def makeEvironmen(confFile):
    global LOG
    logging.config.fileConfig("logger.conf")
    LOG = logging.getLogger("root")
    LOG.debug('This is debug message')
    LOG.info('This is info message')
    LOG.warning('This is warning message')


if __name__=="__main__":
    #info=basicTraffic()
    cf = ConfigParser.ConfigParser()
    cf.read("common.conf")
    confDict=loadConfAsDict("eNodeB.conf")
    pdb.set_trace()
    loadConf("common.conf")
    logging.config.fileConfig("logger.conf")
    LOG = logging.getLogger("root")
    LOG.debug('This is debug message2')
    LOG.info('This is info message2')
    LOG.warning('This is warning message2')
    a=pro.OkumauraHata(1800,10,3)
    a.plotModel(1,3,0.01)