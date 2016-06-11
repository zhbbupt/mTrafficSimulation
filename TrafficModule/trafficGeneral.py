# -*- coding: utf-8 -*-
'''
Created on 2016-06-05 18:15
summary: 用于生成业务
author: zhbbupt
'''


from TrafficModule.basicTraffic import basicTraffic
from PropagationModule.propagationModel import *

def getPathLoss(pathLoss,d,confugure,propModel):
    pathLoss={}
    if d in pathLoss:
        return pathLoss[d]
    else:
        pathLoss[d]=propModel.calLoss(d,confugure)
        return pathLoss[d]

def genSingleTraffic(paras,trafficConf):
    '''
    Summary: 
        生成一个业务        
    Args:
        paras (dict): 计算得到的参数
        trafficConf (dict): 业务配置
    
    Returns:
        TYPE: 返回业务
    '''
    return 0
def makeEve(configue):
    global frequence,recevive_height,transmit_height
    global scene
    global transmit_power,tti
    global simulation_radius



def genTraffic(configure):
    '''
    Summary: 
        均匀生成业务
    Args:
        mapConf (dict): 地图配置信息
        trafficConf(dict): 业务配置信息
        baseConf(dict):基站配置信息
    Returns:
        TYPE: Description
    '''
    #根据配置信息生成环境变量

    #根据地形生成传播模型类
    propModel=OkumauraHata()

    
