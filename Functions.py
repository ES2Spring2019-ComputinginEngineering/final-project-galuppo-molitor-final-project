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
from astropy.table import Table

from DataParsing import * 
Low, Age, LWT, Race, Smoker, PTL, Hypertension, UI, FTV, BWT = readDataFile()
NonSmoker_Birthweights, Smoker_Birthweights = List_Creation2(NonSmoker_Birthweights, Smoker_Birthweights, Smoker)
Race_1, Race_2, Race_3 = List_Creation3(Race_1, Race_2, Race_3, Race)
HypertensionNeg_BW, HypertensionPos_BW = List_Creation2(HypertensionNeg_BW, HypertensionPos_BW, Hypertension)
FTV_0, FTV_1, FTV_2, FTV_3, FTV_4 = List_Creation5(FTV_0, FTV_1, FTV_2, FTV_3, FTV_4, FTV)
UINeg, UIPos = List_Creation2(UINeg, UIPos, UI)

#DATA VISUALIZATION FUNCTIONS - individual risks
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
    
#def Histogram_4(List1, List2, List3, List4, names, bins):
#    colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73']
#    plt.hist([List1, List2, List3, List4], bins = bins, color = colors, label = names)
#    plt.legend()
#    
#def Histogram_2(List1, List2, names, bins): 
#    colors = ['#F0E442', '#009E73'] 
#    plt.hist([List1, List2], bins=bins, color = colors, label = names)
#    plt.legend()

def DensityPlot_2(List1, List2, Label1, Label2, Title):
    plt.figure()
    sns.distplot(List1, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'darkblue', rug = True, label = Label1)
    sns.distplot(List2, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'lightblue', rug = True, label = Label2)
    plt.title(Title)
    plt.xlabel("Birthweight (Grams)")
    plt.show()
    
def DensityPlot_3(List1, List2, List3, Label1, Label2, Label3, Title): 
    plt.figure()
    sns.distplot(List1, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'darkblue', rug = True, label = Label1)
    sns.distplot(List2, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'lightblue', rug = True, label = Label2)
    sns.distplot(List3, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'purple', rug = True, label = Label3)
    plt.title(Title)
    plt.xlabel("Birthweight (Grams)")
    plt.show()
    
def DensityPlot_5(List1, List2, List3, List4, List5, Label1, Label2, Label3, Label4, Label5, Title): 
    plt.figure()
    sns.distplot(List1, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'darkblue', rug = True, label = Label1)
    sns.distplot(List2, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'lightblue', rug = True, label = Label2)
    sns.distplot(List3, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'purple', rug = True, label = Label3)
    sns.distplot(List4, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'lightgreen', rug = True, label = Label4)
    sns.distplot(List5, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'darkgreen', rug = True, label = Label5)
    plt.title(Title)
    plt.xlabel("Birthweight (Grams)")
    plt.show()
    
#DESCRIPTIVE STATISTICS FUNCTIONS - individual risks
def mean_BW(List):
    mean = round(np.mean(List),1)
    return mean

def median_BW(List):
    median = round(np.median(List),1)
    return median

def correlationCoefficient(x_values, y_values):
    return np.corrcoef(x_values, y_values)

def desStatsTable_2(ListAll, List1, List2, Label1, Label2, title):
    print('\n',"Descriptive Statistics Data Table of", title, '\n')
    mothers = 'Number of Mothers', len(ListAll), len(List1), len(List2)
    means = 'Mean Birth Weight (grams)', mean_BW(ListAll), mean_BW(List1), mean_BW(List2)
    medians = 'Median Birth Weight (grams)', median_BW(ListAll), median_BW(List1), median_BW(List2)
    data_rows = [mothers,means, medians]
    t = Table(rows = data_rows, names = ("Statistic", "All Datapoints",Label1, Label2))
    print(t)
#    correlation = correlationCoefficient(x_values, y_values)
    
def desStatsTable_3(ListAll, List1, List2, List3, Label1, Label2, Label3, title):
    print('\n',"Descriptive Statistics Data Table of", title, '\n')
    mothers = 'Number of Datapoints', len(ListAll), len(List1), len(List2), len(List3)
    means = 'Mean Birth Weight (grams)', mean_BW(ListAll), mean_BW(List1), mean_BW(List2), mean_BW(List3)
    medians = 'Median Birth Weight (grams)', median_BW(ListAll), median_BW(List1), median_BW(List2), median_BW(List3)
    data_rows = [mothers,means, medians]
    t = Table(rows = data_rows, names = ("Statistic", "All Datapoints",Label1, Label2, Label3))
    print(t)
    
def desStatsTable_5(ListAll, List1, List2, List3, List4, List5, Label1, Label2, Label3, Label4, Label5, title):
    print('\n',"Descriptive Statistics Data Table of", title, '\n')
    mothers = 'Number of Datapoints', len(ListAll), len(List1), len(List2), len(List3), len(List4), len(List5)
    means = 'Mean Birth Weight (grams)', mean_BW(ListAll), mean_BW(List1), mean_BW(List2), mean_BW(List3), mean_BW(List4), mean_BW(List5)
    medians = 'Median Birth Weight (grams)', median_BW(ListAll), median_BW(List1), median_BW(List2), median_BW(List3), median_BW(List4), median_BW(List5)
    data_rows = [mothers,means, medians]
    t = Table(rows = data_rows, names = ("Statistic", "All Datapoints",Label1, Label2, Label3, Label4, Label5))
    print(t)