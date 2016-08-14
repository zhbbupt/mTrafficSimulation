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

import random
import numpy as np
from TrafficMoudule import traffic

def gen_traffic_list(time_serial_num,traffic_num,traffic_data_mean_size):
    traffic_list = [0]*time_serial_num
    #生成时序包络
    mu = int(random.uniform(0, time_serial_num))
    sigma = random.uniform(1,6)
    #每一时序生成随机的业务数
    i = 0
    while (i<time_serial_num): 
        tmp_time_serial = int(random.gauss(mu, sigma))
        if tmp_time_serial < time_serial_num and tmp_time_serial >=0:
            traffic_list[tmp_time_serial] = traffic_list[tmp_time_serial]+1
            i+=1
    plotLine(range(0,len(traffic_list)),traffic_list)
    #每个业务生成随机的数据块
    mu = traffic_data_mean_size
    sigma = traffic_data_mean_size*0.1
    floor_data_size = mu - 3*sigma
    ceil_data_size = mu + 3*sigma

    traffic_entity_list=[[]]*time_serial_num
    for index,k in enumberate(traffic_list):
        i=0
        while (i<k):
            data_size = int(random.gauss(mu, sigma))
            if data_size>floor_data_size and data_size < ceil_data_size :  
                traffic_entity_list[index] 
                i=i+1
    return traffic_entity_list

def GeneratePointInCycle(point_num,radius)
    #ori_coordinates=[]
    polo_coordinates=[]
    for i in range(1, point_num+1):
        theta = random.random()*2*pi;
        r = random.uniform(0, radius)**0.5
        polo_coordinates.append([r,theta])
        #x = math.sin(theta)* r
        #y = math.cos(theta)* r
    return polo_coordinates
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
    ## 加载仿真配置文件
    simulate_conf = loadConfAsDict("simulate.conf")
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
    traffic_entity_list=gen_traffic_list(ime_serial_num,traffic_num,traffic_data_mean_size)
    # 撒业务

    # 计算业务优先级
    
    # 调度业务
    # 统计数据
    # 画图

if __name__ == '__main__':
    LTE_traffic_simulation_sample()




