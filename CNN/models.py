import torch
import torch.nn as nn
import torch.nn.functional as F

class ConvStft(nn.Module):
    def __init__(self):
        super(ConvStft, self).__init__()

        self.conv_1 = nn.Conv2d(1, 32, (3, 3), stride=1)
        self.conv_2 = nn.Conv2d(32, 64, (3, 3), stride=1)
        self.conv_3 = nn.Conv2d(64, 128, (3, 3), stride=1)
        self.conv_4 = nn.Conv2d(128, 256, (3, 3), stride=1)

        self.fc_1 = nn.Linear(99, 64)
        self.fc_2 = nn.Linear(64, 5)

        self.pool_1 = nn.MaxPool2d((2, 2), stride=2)
        self.pool_2 = nn.MaxPool2d((2, 2), stride=2)
        self.pool_3 = nn.MaxPool2d((2, 2), stride=2)
        self.pool_4 = nn.MaxPool2d((2, 2), stride=2)

        self.bn_1 = nn.BatchNorm2d(32)
        self.bn_2 = nn.BatchNorm2d(64)
        self.bn_3 = nn.BatchNorm2d(128)
        self.bn_4 = nn.BatchNorm2d(256)
        self.bn_5 = nn.BatchNorm1d(64)

    def forward(self, x):
        x = self.conv_1(x)
        x = self.bn_1(x)
        x = F.leaky_relu(x)
        x = self.conv_2(x)
        x = self.bn_2(x)
        x = F.leaky_relu(x)
        x = self.conv_3(x)
        x = self.bn_3(x)
        x = F.leaky_relu(x)
        x = self.conv_4(x)
        x = self.bn_4(x)
        x = F.leaky_relu(x)

        x = x.view(-1, 99)
        x = self.fc_1(x)
        x = self.bn_5(x)
        x = F.leaky_relu(x)
        x = self.fc_2(x)
        x = F.softmax(x)

        return x



