# -*- coding:utf-8 -*-
'''
created on : 4/28/2016 3:19:02 PM
fileName   : baseModule.py
author     : zhbbupt
TODO       : 本模块是业务源模型的基类
'''
import  Utils.mathTools
#业务源基类
class basicTraffic(object):
    blockSize=0     #要传输的字节数
    delayCommandLevel=1     #时延要求等级1最高
    packageNumToSent=1        #待发送的数据包
    packageNumSented=0        #已发送的数据包
    packageReserve=1        #还需发送的数据包
    percentPackageToSent=1     #本轮要发送的数据包
    percentPackageArrive=1      #经过信道随机丢包后到达接收端的数据包大小
    percentPackageSented=1     #本轮已发送的数据包
    percentPackageLoss=0       #本轮丢包数
    packageSize=4       #默认每个包大小为4kb，调制方式不同，大小不同
    power=45        #发射功率，单位dbm
    loss=0      #路径损失，db
    sinr=0      #信噪比
    RTT=1       #回路相应时间
    initRTO=2   #初始超时重传计时器
    RTO=2       #超时重传计时器
    waitTime=0      #等待时间
    maxRTOStage=6       #最大超时重传阶数
    RTOFactor=2 #超时重传计时器增长因子
    
    maxWss=16
    status=[1,2]       #当前业务所属状态[w,Wss],w:当前发送窗口大小,Wss当前慢启动门限
    QAM=6       #调制方式，默认2^6，即64QAM，QPSK：2,16QAM：4



    def __init__(self,Conf):
        self.delayCommandLevel=Conf["delayCommandLevel"]
        self.maxWss=Conf["maxWss"]
        self.maxRTOStage=Conf["maxRTOStage"]
    # 下一个状态
    # 当有发生丢包时，若此时发送窗口非常大且丢包数很少，则认为发生了随机丢包，执行快速恢复/快速重传
    # 算法,此时将发送窗口减半，执行拥塞避免过程;若丢包数量大，则认为网络发生拥塞，TCP会等待重传超时
    # 然后转入慢启动过程，同时慢启动门限设置为当前拥塞窗口的一般w/2。若重传定时器超时后第一次发包扔
    # 发生丢包，TCP则将超时定时器加倍，继续重传该数据包，即TCP进入超时指数退避状态，退避阶数为6阶，
    # 当退避过程执行至最大退避时长时若仍未发送成功，则发送数据包发送失败  
    # @action：1：发送窗口正常增长；2：拥塞避免,快速重传状态；3：拥塞退避，超时状态
    def nextStatus(self,action):
        #正常状态,发送窗口增长 [w,Wss]->[w+1,Wss]
        if action==1:
            if status[0]==status[1]:  
                if status[1]<maxWss:
                    status[0]+=1
                    status[1]+=1
                else:
                    status[0]+=1
            elif status[0]<status[1] : 
                status[0]=min(status[0]*2,status[1])
                status[1]=max(status[0],status[1])
            else:
                status[1]=status[0]
        #正常状态,快速重传[w,Wss]->[w/2,w/2]
        elif action==2:
            status[0]=status[0]/2
            if  status[0]<2:
                status[0]=0
                status[1]=2
            else:
                status[1]=status[0]
        #正常状态,进入超时状态[w,Wss]->[0,w/2]
        elif action==3:
            status[1]=1
            status[0]=status[0]>>1
            while(status[0]>0):
                status[1]=status[1]<<1
                status[0]=status[0]>>1
            status[0]=0
        #超时状态，发送成功，进入正常状态 [0,Wss]->[1,Wss]
        elif action==4:
            status[0]=1
        #超时状态，发送失败，进入退避状态 [0,Wss]->[1,0]
        elif action==5:
            status[0]=1
            status[1]=0
        #退避状态，发送成功，进入正常状态 [w,0]->[1,2]
        elif action==6:
            status[0]=1
            status[1]=2
        #退避状态，发送失败，退避时间增长 [w,0]->[w+1,0]
        elif action==7:
            status[0]+=1
            status[1]=0
    #根据当前状态更新参数
    def refreshPrams(self):
        #退避状态
        if self.status[1]==0:
            self.RTO*=self.RTOFactor
        #超时状态
        elif self.status[0]==0:
            self.packageNumToSent-=self.percentPackageSented
            self.percentPackageToSent=1
        #正常状态
        else:
            self.packageNumToSent-=self.percentPackageSented
            self.percentPackageToSent=min(self.status[0],self.packageNumToSent)
    #状态转移函数,根据调度的包转移
    def takeAction(self):
        #发送成功
        if self.percentPackageSented==self.percentPackageToSent:
            if self.status[0]==0:
                self.nextStatus(4)
            elif self.status[1]==0:
                self.waitTime=0
                self.RTO=self.initRTO
                self.nextStatus(6)
            else:
                self.nextStatus(1)
        #发送失败
        else:
            if self.status[0]==0:
                self.nextStatus(5)
            elif self.status[1]==0:
                # 发送失败，记录等待时间，如果到达RTO时间则进入下一阶退避过程
                self.waitTime+=1
                if self.waitTime==self.RTO:
                    self.nextStatus(7)
            else:
                if self.status[0]<4 or (self.status[0]>=4 and self.status[0]<10 and self.percentPackageLoss>=2) or (self.status[0]>=10 and self.percentPackageLoss>=3):
                    self.nextStatus(3)
                else:
                    self.nextStatus(2)
    # 这是提供给基站调度的接口
    # schPackageNum：基站调度的包数量
    def schedule(self,schPackageNum):
        self.percentPackageSented=schPackageNum
        self.percentPackageLoss=self.percentPackageToSent-schPackageNum
        self.packageNumSented+=schPackageNum
        self.packageReserve-=schPackageNum
        self.takeAction()
        self.refreshPrams()
    # 这是提供给基站接口，判断该业务是否失败
    def isFailed(self):
        if self.status[1]==0 and self.status[0]>self.maxRTOStage:
            return True
        else:
            return False









