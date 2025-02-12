import numpy as np
import torch
import torch.nn as nn
from torch.autograd import Variable

def EntropyLoss(input_):
    mask = input_.ge(0.000001)
    mask_out = torch.masked_select(input_, mask)
    entropy = -(torch.sum(mask_out * torch.log(mask_out)))
    return entropy / float(input_.size(0))

def DANN(features, ad_net, grl_layer, iter_num=1, use_gpu=True):
    ad_out = ad_net(grl_layer(features, iter_num))
    batch_size = ad_out.size(0) // 2
    dc_target = Variable(torch.from_numpy(np.array([[1]] * batch_size + [[0]] * batch_size)).float())
    if use_gpu:
        dc_target = dc_target.cuda()
    #print("Print before loss")
    #print(ad_out.view(-1))
    #print("")
    #print("")
    #print("")
    #print("")
    #print("")
    #print("")
    #print("")
    #print("")
    #print("")
    #print("")
    #print(dc_target.view(-1))
    return nn.BCELoss()(ad_out.view(-1), dc_target.view(-1))

