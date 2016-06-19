# -*- coding: utf-8 -*-
'''
created on 2016-06-19 17:25
summary: 计算链路损耗
author: zhbbupt
'''
import pdb
import pickle
import pprint 
from PropagationModule.propagationModel import OkumauraHata

def CalPathLoss(propagation_model,scene,d):
    return propagation_model.calLoss(d,scene)
def SavePathLoss(path_loss_dict,file_path):
    output_file = open(file_path, 'wb')
    pickle.dump(path_loss_dict, output_file)
    output_file.close()
def CalZonePathLoss(propagation_model,distance_scope,scene,accuracy):
    path_loss_dict={}
    tmp=int(round((distance_scope[1]-distance_scope[0])/accuracy))
    d=distance_scope[0]
    for i in range(0,tmp,1):
        d=d+accuracy
        d=round(d,4)
        d_string="%.3f"%d
        path_loss_dict[d_string]=CalPathLoss(propagation_model,scene,d)
    return path_loss_dict
def GetPropagationModel(model_name,init_params):
    if model_name == "OkumauraHata":
        model=OkumauraHata(init_params["frequence"],init_params["transmit_height"],init_params["recevive_height"])
        return model
def LoadPathLoss(file_path="model.buff"):
    input_file = open(file_path, 'rb')
    path_loss_dict = pickle.load(input_file)
    return path_loss_dict
def CaculatePathLoss(model_name,params,save_as_file=True,save_model_path="model.buff"):
    model=GetPropagationModel(model_name,params)
    path_loss_dict={}
    path_loss_dict=CalZonePathLoss(model,params["distance_scope"],params["scene"],params["accuracy"])
    if save_as_file == True:
        SavePathLoss(path_loss_dict,save_model_path)
    # pdb.set_trace()
    # pprint.pprint(path_loss_dict)
    return path_loss_dict
