# -*- coding: utf-8 -*-
'''
created on 2016-07-23 16:34
summary: To Generize random number
author: zhbbupt
'''
import random
import numpy as np

class RandomGenerator(object):
    def __init__(self):
        random.seed()
    def GenerateGaussRand(mu,sigma):
        return  random.gauss(mu, sigma)
    def GenerateParetovariate(alpha):
        return random.paretovariate(alpha)  
    def GenerateExpovariate(lambd):
        return random.expovariate(lambd)   
    def GenerateBetavariate(alpha,beta):
        return random.expovariate(alpha,beta)
    def GenGaussList(mu,sigma,number):
        return np.random.normal(mu,sigma,number)
    def GenParetoList(alpha,number):
        return np.random.pareto(alpha,number)
