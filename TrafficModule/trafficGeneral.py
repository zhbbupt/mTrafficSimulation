# -*- coding: utf-8 -*-
'''
Created on 2016-06-05 18:15
summary: 用于生成业务
author: zhbbupt
'''


from TrafficModule.basicTraffic import basicTraffic
from PropagationModule.propagationModel import *
from random import *
import math
import copy

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
def makeEve(configue,params):
    global frequence,recevive_height,transmit_height
    global scene
    global transmit_power,tti
    global cell_radius
    global density
    global traffic_num
    global rand
    global PI
    PI=3.14159
    frequence=configue.conf["eNodeBConf"]["frequence"]
    recevive_height=configue.conf["eNodeBConf"]["height"]
    transmit_height=configue.conf["commonTerminal"]["height"]
    scene=configue.conf["mapConf"]["scene"]
    transmit_power=configue.conf["eNodeBConf"]["transmit_power"]
    tti=configue.conf["eNodeBConf"]["tti"]
    cell_radius=configue.conf["mapConf"]["dictance"]
    density=configue.conf["trafficConf"]["commonTraffic"]["density"]

    current_tti=params["currentTTI"]
    rand=Random()
    rand.seed(tti)
    traffic_num=round(rand.gauss(density, density/5))*PI*cell_radius*cell_radius
    traffic_conf=configue.conf["trafficConf"]
    single_traffic_conf=copy.copy(traffic_conf)
    

def genTraffic(configure,params):
    """
    Summary: 生成业务
    
    Args:
        configure (Dict) : 基础配置
        params (Dict) : 运行参数
    
    Returns: 
        TYPE : Description
    """
    #根据配置信息生成环境变量
    makeEve(configure,params)
    #根据地形生成传播模型类
    propModel=OkumauraHata(frequence,transmit_height,recevive_height)
    #生成业务
    trafficList=[]
    tmp=cell_radius*cell_radius
    for i in range(1,traffic_num):
        distance=math.sqrt(random.uniform(0.0001,tmp))
        theta=random.uniform(0,2*PI)
        loss=propModel.calLoss(distance,scene)

        pass



    
