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

from numpy import random
from scipy.stats import *
from Utils.plotTools import *
from scipy import stats
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
from src.PathLossTools  import * 

def standard_normal_rand():
    pf = {}
    for i in range(0, 100000):
        x = round(random.poisson(1), 2)
        if(pf.has_key(x)):
            pf[x] += 1
        else:
            pf[x] = 1
    X = []
    Y = []
    for i in pf.keys():
        X.append(i)
        Y.append(pf[i])
    # pdb.set_trace()
    plotPoint(X, Y, '*', 'd/km', 'Loss/dB', title='OkumauraHata')


def standard_normal_rand_2():
    s = np.random.poisson(5, 100000)
    #s = np.random.poisson(lam=(100., 500.), size=(100, 2))
    count, bins, ignored = plt.hist(s, 15, normed=True)
    plt.show()


def makeEvironmen(confFile):
    """Summary

    Args:
        confFile (TYPE): Description

    Returns:
        TYPE: Description
    """
    global LOG
    logging.config.fileConfig("logger.conf")
    LOG = logging.getLogger("root")
    LOG.debug('This is debug message')
    LOG.info('This is info/ message')
    LOG.warning('This is warning message')
if __name__ == "__main__":

    params={}
    params["distance_scope"]=[1,3]
    params["scene"]=0
    params["accuracy"]=0.1
    params["frequence"]=1800
    params["transmit_height"]=30
    params["recevive_height"]=3
    model_name = "OkumauraHata"
    CaculatePathLoss(model_name, params)
    path_loss_dict=LoadPathLoss()

    pdb.set_trace()

    conf = Configure("common.conf")



    # pdb.set_trace()

    a = {"a": 10}
    print(a.has_key("a"))
    b = 'a'
    print(a[b])
    print('a' in a)

    # info=basicTraffic()
    standard_normal_rand_2()
    cf = ConfigParser.ConfigParser()
    cf.read("common.conf")
    confDict = loadConfAsDict("eNodeB.conf")

    # pdb.set_trace()
    conf = Configure("common.conf")

    loadConf("common.conf")

    logging.config.fileConfig("logger.conf")
    LOG = logging.getLogger("root")
    LOG.debug('This is debug message2')
    LOG.info('This is info message2')
    LOG.warning('This is warning message2')
    a = pro.OkumauraHata(1800, 10, 3)
    a.plotModel(0.1, 5, 0.01)
