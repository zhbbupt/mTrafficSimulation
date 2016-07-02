# -*- coding: utf-8 -*-
'''
Created on 2016-07-02 17:56

Summary :   Traffic Generator

Author  :   zhbbupt

Email   :   zhb_bupt@163.com

'''

from TrafficModel import nonGBRTraffic   
import random
import math

def TrafficGenerator(traffic_param,distribute_param):
    traffic_num = 0
    distribute_type =  distribute_param["distribute_type"]
    if distribute_type == "Gauss":
        mean = distribute_param["mean"]
        sigma = distribute_param["sigma"]
        traffic_num = int(ceil(random.gauss(mean,sigma)))
    traffic_list = []
    traffic_type = traffic_param["traffic_type"]
    if traffic_type = "nonGBR":
        for i in range(0,traffic_num):
            tmp = nonGBRTraffic()
            traffic_list.append(tmp)

    return traffic_list