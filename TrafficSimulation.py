# -*- coding: utf-8 -*-
'''
created on 2016-07-12 17:44
summary: use to simulate traffic interbehavior
author: zhbbupt
'''

from TrafficMoudule import TrafficMoudule
from TrafficModule import TrafficGenerator
from PropagationModule import propagationModel
from PropagationModule import PathLossTools  
from Utils import *
from BaseModule import LteNodeB


from numpy import random
from scipy.stats import *
from Utils.plotTools import *
from scipy import stats
import string
import os
import sys
import pdb



def LTE_traffic_simulation_sample():
    # 加载日志文件
    logging.config.fileConfig("logger.conf")
    LOG = logging.getLogger("root")
    LOG.info('start simulation')
    # 加载配置文件
    ## 加载基站配置文件    
    eNodeB_conf = loadConfAsDict("eNodeB.conf")
    ## 加载业务配置文件
    traffic_conf = loadConfAsDict("traffic.conf")
    ## 加载终端配置文件
    terminal_conf = loadConfAsDict("terminal.conf")
    ## 加载地图配置文件
    map_conf = loadConfAsDict("map.conf")
    # 计算路损
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
    # 生成业务
    # 计算业务优先级
    # 调度业务
    # 统计数据
    # 画图

if __name__ == '__main__':
    LTE_traffic_simulation_sample()




