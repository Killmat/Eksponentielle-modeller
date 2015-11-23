#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# Import af visual og visual graph til senere brug.
from visual import *
from visual.graph import *
# Data sættet som er leveret fra opgaveoplægget
data_set = [[0, 15], [20, 16], [40, 18], [60, 19], [80, 22], [100, 24], [140, 31], [160, 42], [180, 49], [200, 67],
            [220, 78], [240, 90], [260, 105], [280, 109], [300, 122], [320, 125]]
# Data sættets x-værdier sættes i en list
x = []
for i in range(0, len(data_set)):
    x.append(data_set[i][0])
print x
# Data sættets y-værdier sættes i en list
y = []
for i in range (0, len(data_set)):
    y.append(data_set[i][1])
print y

#Tegning af graf
curve = gcurve(color=color.cyan)

for n in range(0, len(data_set)):
    curve.plot(pos=(x[n], y[n]))
