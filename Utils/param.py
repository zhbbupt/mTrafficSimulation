# -*- coding: utf-8 -*-
'''
Created on 2016-07-03 15:36

Summary: params class

Author: zhbbupt

'''
import pdb

class BaseParams(object):
    def __init__(self,info="Base Params"):
        self._info=info
    def getInfo(cls):
        return cls._info
class GaussDistributeParams(BaseParams):
    def __init__(self,mu,sigma,info="Gauss Distribute Params"):
        self.mu = mu
        self.sigma = sigma 
        super(GaussDistributeParams,self).__init__(info)


class TrafficParams(BaseParams):
    _instance = None
    @staticmethod
    def getInstance():
        if TrafficParams._instance != None:
            return TrafficParams._instance
        else:
            print "%s hasn't init"%(TrafficParams.__name__)
    def __init__(self,traffic_param):
        info = "params  which is used to general single traffic" if not traffic_param.has_key("info") else traffic_param["info"]

        super(TrafficParams,self).__init__(info)
        if traffic_param["distribute_type"] == "Gauss":
            mu = traffic_param["mu"]
            sigma = traffic_param["sigma"]
            self.distribute_params = GaussDistributeParams(mu,sigma)
        self.package_size = traffic_param["package_size"]
        TrafficParams._instance = self
        print TrafficParams._instance


