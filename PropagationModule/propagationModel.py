# -*- coding:utf-8 -*-
'''
created on : 5/1/2016 3:57:37 PM
fileName   : propagationModel.py
author     : zhbbupt
TODO       : 传播模型
'''
import math
from Utils.plotTools import plotLine
# Okumura-Hata模型是根据测试数据统计分析得出的经验公式
# 应用频率在150~1500MHz之间,适用于小区半径大于1 km的宏蜂窝系统
# 基站有效天线高度在30 ~200 m之间，移动台有效天线高度在1 ~10 m之间
class OkumauraHata(object):
    fc=1800     #工作频率（MHz）
    logfc=3.255    #工作频率（MHz）的对数 
    hte=10      #基站天线高度（m）
    loghte=1        #基站天线高度（m）的对数
    hre=3       #接收天线高度（m）
    loghre=0.477        #接收天线高度（m）的对数
    def set_fc(self,fc):
        self.fc=fc
        self.logfc=math.log10(fc)
    def set_hte(self,hte):
        self.hte=hte
        self.loghte=math.log10(hte)
    def set_hre(self,hre):
        self.hre=hre
        self.loghre=math.log10(hre)
    def __init__(self,fc=1800,hte=10,hre=3):
        self.set_fc(fc)
        self.set_hte(hte)
        self.set_hre(hre)
    # 计算有效接收天线修正因子
    # scene：场景，1:大城市市区，2：中小城市市区，3：郊区，4：农村
    def calHre(self,scene):
        if scene==2:
            return (1.11*self.logfc-0.7)*hre-(1.56*self.logfc-0.8)
        else:
            if self.fc<=300:
                return 8.29*self.loghre*self.loghre+3.109*self.loghre-0.8086
            else:
                return 3.2*self.loghre*self.loghre+6.848*self.loghre-1.306
    # 计算小区类型修正因子
    # scene：场景，1:大城市市区，2：中小城市市区，3：郊区，4：农村
    def calCcell(self,scene):
        if scene==1 or scene==2:
            return 0
        elif scene==3:
            return -2*self.logfc*self.logfc+5.789*logfc-9.589
        else:
            return -4.78*self.logfc*self.logfc+18.33*self.logfc-40.98
    # 计算链路损耗
    # d：距离（km）
    # scene：场景，1:大城市市区，2：中小城市市区，3：郊区，4：农村
    # Cterrain：地形校正因子
    def calLoss(self,d,scene=1,Cterrain=0):
        if d<=0:
            return 0
        logd=math.log10(d)
        Altha_hre=self.calHre(scene)
        Ccell=self.calCcell(scene)
        #loss=69.55+26.16*self.logfc-13.82*self.loghte-Altha_hre+(44.9-6.55*loghte)*logd+Ccell+Cterrain
        loss=69.55+26.16*self.logfc-13.82*self.loghte-Altha_hre+(44.9-6.55*self.loghte)*logd+Ccell+Cterrain
        return loss

    def plotModel(self,dLow,dHigh,accuracy,scene=1,Cterrain=0):
        len=dHigh-dLow
        num=int(round(len/accuracy))
        d=[]
        for i in range(0,num):
            d.append(dLow+i*accuracy)
        loss=[]
        for i in d:
            loss.append(self.calLoss(i,scene,Cterrain))
        plotLine(d,loss,'r','d/km','Loss/dB',title='OkumauraHata')


