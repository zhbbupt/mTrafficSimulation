# -*- coding: utf-8 -*-
'''
Created on 2016-06-05 17:28
summary: 
author: zhbbupt
'''

class LteNodeB(object):


    def __init__(self,LTE_eNodeB_params):
        self.params = LTE_eNodeB_params
    def cal_priority(self,traffic_list):
        sum_data = 0.0
        for traffic in traffic_list:
            sum_data = traffic.data_size + sum_data
        for traffic in traffic_list : 
            traffic.priority = 0.5 * traffic.level + 0.5 * traffic.delay_tti + traffic.data_size/sum_data + 10 ** ((float)traffic.sinr/10)

    def shedule(self,traffic_list , lte_base):
        LteSheduler.cal_priority(traffic_list)    
        
