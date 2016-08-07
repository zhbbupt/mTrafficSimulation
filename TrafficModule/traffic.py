# -*- coding: utf-8 -*-
'''
created on 2016-06-19 15:44
summary: 这是普通业务模块
author: zhbbupt
'''


class traffic(object):

    # def __init__(self, arg):
    #     super(traffic, self).__init__()
    #     self.distance = arg["distance"]
    #     self.theta=arg["theta"]
    #     self.block_size=arg["block_size"]
    #     self.priority=arg["priority"]
    #     self.traffic_type=arg["traffic_type"]
    #     self.transmit_power=arg["transmit_power"]
    #     self.loss=arg["loss"]
    #     self.sinr=arg["sinr"]

    def __init__(self,traffic_type):
        self.distance = 0.001
        self.theta = 0
        self.block_size = 0
        self.priority = 1
        self.traffic_type = traffic_type
        self.transmit_power = 46
        self.loss = 0
        self.sinr = 46
















