#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:40:00 2019

@author: victoriamolitor
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab
from numpy import arange, array, ones
from scipy import stats 

from DataParsing import * 
Low, Age, LWT, Race, Smoker, PTL, Hypertension, UI, FTV, BWT = readDataFile()


#def graphData(x_values, y_values, classification, title): 
#    plt.figure
#    plt.title(title)
#    plt.plot(x_values[classification == 0], y_values[classification == 0], "b.", label = 'Class 0: Condition is False')
#    plt.plot(x_values[classification == 1], y_values[classification == 1], "r.", label = 'Class 1: Condition is True')
#    plt.legend()
#    plt.show()
#
#def linearFit(x_values, y_values): 
#    slope, intercept, r_value, p_value, std_err = stats.linregress(x_values, y_values)
#    line = slope*x_values + intercept
#    plt.plot(x_values, y_values, 'b.', Age, line)
#    plt.show()
#
#def linearFit_Conditions(x_values, y_values, classification): 
#    slope, intercept, r_value, p_value, std_err = stats.linregress(x_values, y_values)
#    line = slope*x_values + intercept
#    plt.plot(x_values[classification == 0], y_values[classification == 0], "b.", label = 'Class 0: Condition is False')
#    plt.plot(x_values[classification == 1], y_values[classification == 1], "r.", label = 'Class 1: Condition is True')
#    plt.plot(Age, line)
#    plt.legend()
#    plt.show()
    
def graphNumerical(x_values, y_values, classification, title): 
    plt.figure
    plt.title(title)
    plt.plot(x_values[classification == 0], y_values[classification == 0], "b.", label = 'Class 0: Condition is False')
    plt.plot(x_values[classification == 1], y_values[classification == 1], "r.", label = 'Class 1: Condition is True')
    plt.legend()
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_values, y_values)
    line = slope*x_values + intercept
    plt.plot(x_values, line)
    plt.show()
    
#defUNKNOWN

#def graphCategorical
    
def correlationCoeddicient(x_values, y_values):
    return np.corrcoef(x_values, y_values)