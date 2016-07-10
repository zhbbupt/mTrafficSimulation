# -*- coding: utf-8 -*-
'''
created on 2016-07-09 18:19
summary: LTE sheduler
author: zhbbupt
'''


class LteSheduler(object):
    @staticmethod
    def cal_priority(traffic_list):
        sum_data = 0.0
        for traffic in traffic_list:
            sum_data = traffic.data_size + sum_data
        for traffic in traffic_list : 
            traffic.priority = 0.5 * traffic.level + 0.5 * traffic.delay_tti + traffic.data_size/sum_data + 10 ** ((float)traffic.sinr/10)

    @staticmethod
    def shedule(traffic_list , lte_base):
        LteSheduler.cal_priority(traffic_list)


