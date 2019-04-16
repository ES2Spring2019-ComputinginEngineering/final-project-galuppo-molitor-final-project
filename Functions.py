#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:40:00 2019

@author: victoriamolitor
"""

from DataParsing import * 
Low, Age, LWT, Race, Smoker, PTL, Hypertension, UI, FTV, BWT = readDataFile()
print(Low)


def graphData(x_values, y_values, classification): 
    plt.figure
    plt.plot(x_values[classification == 0], y_values[classification == 0], "b.", label = 'Class 0: Condition is False')
    plt.plot(x_values[classification == 1], y_values[classification == 1], "r.", label = 'Class 1: Condition is True')
    plt.legend()
    plt.show()

graphData(FTV, BWT, Low)