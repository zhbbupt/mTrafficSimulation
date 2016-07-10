# -*- coding: utf-8 -*-
'''
Created on 2016-07-02 17:56

Summary :   Traffic Model

Author  :   zhbbupt

Email   :   zhb_bupt@163.com

'''


class nonGBRTraffic_old(object):
    # data_size = 1
    # package_num = 1

    # path_loss = 0

    # level=1

    def __init__(self,traffic_param):
        self.data_size = traffic_param["data_size"]
        self.package_num = traffic_param["package_num"]
        self.path_loss = traffic_param["path_loss"]
        self.level = traffic_param["level"]

class nonGBRTraffic(object):
    # data_size = 1
    # package_num = 1

    # path_loss = 0

    # level=1

    def __init__(self,traffic_param):
        self.data_size = traffic_param["data_size"]
        self.package_num = traffic_param["package_num"]
        self.path_loss = traffic_param["path_loss"]
        self.level = traffic_param["level"]
        self.delay_tti = traffic_param["delay_tti"]
        self.priority = self.level
        self.transmit_power = traffic_param["transmit_power"]
        self.interfere = traffic_param["interfere"]
        self.sinr = self.transmit_power - self.path_loss - self.interfere
