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

    def sort_traffic(self,traffic_a,traffic_b):
        return cmp(traffic_a.priority,traffic_b.priority)

    def shedule(self,traffic_list , lte_base):
        LteSheduler.cal_priority(traffic_list)    
        traffic_list.sort(self.sort_traffic)
        self.fail_user = []
        self.shedule_data = []
        tmp_fail_user = len(traffic_list)
        tmp_shedule_data = 0
        tmp_successs_user = 0
        # 调用业务
        for traffic in traffic_list:
            tmp_shedule_RB = traffic.data_size/self.params.RB_size 
            if (tmp_successs_user > self.params.max_user) or (tmp_shedule_RB > self.params.RB_num):
                break
            else:
                tmp_shedule_data = tmp_shedule_data + traffic.data_size
                tmp_successs_user = tmp_successs_user + 1
        self.shedule_data.append(tmp_shedule_data)
        tmp_fail_user = tmp_fail_user - tmp_successs_user
        self.fail_user.append(tmp_fail_user)
        


