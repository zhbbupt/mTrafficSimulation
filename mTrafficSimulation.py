# -*- coding:utf-8 -*-
'''
Created on : 4/28/2016 1:48:58 PM
fileName   : mTrafficSimulation.py
author     : zhbbupt
TODO       : 
'''
from TrafficModule.basicTraffic import basicTraffic
import PropagationModule.propagationModel as pro
import logging
import logging.config
import ConfigParser
import string
import os
import sys
import pdb
from Utils.configTools import loadConfAsDict
from loadConf import *

import random
import scipy.stats as ss


def standard_normal_rand():
    while True:
        X = random.uniform(-3.0, 3.0)
        Y = random.uniform(0.0, 0.5)
        if Y < ss.norm.pdf(X):
            return X
    plotLine(X,Y,'r','d/km','Loss/dB',title='OkumauraHata')


def makeEvironmen(confFile):
    global LOG
    logging.config.fileConfig("logger.conf")
    LOG = logging.getLogger("root")
    LOG.debug('This is debug message')
    LOG.info('This is info/ message')
    LOG.warning('This is warning message')
if __name__ == "__main__":
    # info=basicTraffic()
    standard_normal_rand()
    cf = ConfigParser.ConfigParser()
    cf.read("common.conf")
    confDict = loadConfAsDict("eNodeB.conf")

    loadConf("common.conf")
    logging.config.fileConfig("logger.conf")
    LOG = logging.getLogger("root")
    LOG.debug('This is debug message2')
    LOG.info('This is info message2')
    LOG.warning('This is warning message2')
    a = pro.OkumauraHata(1800, 10, 3)
    a.plotModel(1, 3, 0.01)
