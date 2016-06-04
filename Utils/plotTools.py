# -*- coding:utf-8 -*-
'''
created on : 5/1/2016 3:54:08 PM
fileName   : plotTools.py
author     : zhbbupt
TODO       : 画图工具
'''
import numpy as np
from matplotlib.pylab import plt
def plotLine(x,y,type='r',xlabel='x',ylabel='y',title='y of x function'):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(x,y,type)
    plt.legend()
    plt.show()
