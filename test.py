import torch
import torch.nn as nn

model = torch.load_('/home/user/PycharmProjects/ncf-pytorch/model/NeuMF.pth')
for param in model.parameters():
    print(param)
