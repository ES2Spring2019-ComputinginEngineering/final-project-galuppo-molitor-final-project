#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:40:00 2019

@author: victoriamolitor
"""
from matplotlib import pylab
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange, array, ones
from scipy import stats 
from astropy.table import Table
import statistics

from DataParsing import * 
Low, Age, LWT, Race, Smoker, PTL, Hypertension, UI, FTV, BWT = readDataFile()
NonSmoker_Birthweights, Smoker_Birthweights = List_Creation2(NonSmoker_Birthweights, Smoker_Birthweights, Smoker, BWT)
Race_1, Race_2, Race_3 = List_Creation3(Race_1, Race_2, Race_3, Race, BWT)
HypertensionNeg_BW, HypertensionPos_BW = List_Creation2(HypertensionNeg_BW, HypertensionPos_BW, Hypertension, BWT)
FTV_0, FTV_1, FTV_2, FTV_3, FTV_4 = List_Creation5(FTV_0, FTV_1, FTV_2, FTV_3, FTV_4, FTV, BWT)
UINeg, UIPos = List_Creation2(UINeg, UIPos, UI, BWT)
Normal_BW, Low_BW =List_Creation2(Normal_BW, Low_BW, Low, BWT)
PTL_0, PTL_1, PTL_2, PTL_3 = List_Creation4(PTL_0, PTL_1, PTL_2, PTL_3, PTL, BWT)
All_Birthweights = List_Creation1(All_Birthweights, BWT)
Smoker_Low = Chi_Square_2(Low, Smoker)
Hypertension_Low = Chi_Square_2(Low, Hypertension)
UI_Low = Chi_Square_2(Low, UI)
Race_Low = Chi_Square_3(Low, Race)
PTL_Low = Chi_Square_4(Low, PTL)
FTV_Low = Chi_Square_5(Low, FTV)
Neg_UI_Neg_S, Neg_UI_Pos_S, Pos_UI_Neg_S, Pos_UI_Pos_S = Multi_Factor(Neg_UI_Neg_S, Neg_UI_Pos_S, Pos_UI_Neg_S, Pos_UI_Pos_S, UI, Smoker, BWT)
Neg_H_Neg_S, Neg_H_Pos_S, Pos_H_Neg_S, Pos_H_Pos_S = Multi_Factor(Neg_H_Neg_S, Neg_H_Pos_S, Pos_H_Neg_S, Pos_H_Pos_S, Hypertension, Smoker, BWT)
Neg_UI_Neg_H, Neg_UI_Pos_H, Pos_UI_Neg_H, Pos_UI_Pos_H = Multi_Factor(Neg_UI_Neg_H, Neg_UI_Pos_H, Pos_UI_Neg_H, Pos_UI_Pos_H, UI, Hypertension, BWT)
Normal_Ages, Low_Ages = List_Creation2(Normal_Ages, Low_Ages, Low, Age)
Normal_NW, Low_NW = List_Creation2(Normal_NW, Low_NW, Low, LWT)

def titlePrint(title):
    print('\n',"-------------------------------------------------------------------------------------")
    print('\n', title, '\n')
    print("-------------------------------------------------------------------------------------")

#DATA VISUALIZATION FUNCTIONS - individual variables
def graphNumerical(x_values, y_values, classification, title): 
    plt.figure
    plt.title(title)
    plt.plot(x_values[classification == 0], y_values[classification == 0], "b.", label = 'Class 0: Normal Birthweight')
    plt.plot(x_values[classification == 1], y_values[classification == 1], "r.", label = 'Class 1: Low Birthweight')
    plt.legend()
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_values, y_values)
    line = slope*x_values + intercept
    plt.plot(x_values, line)
    plt.ylabel("Birthweight (Grams)")
    plt.show()
    print("The correlation coefficient for this line of best fit is", round(correlationCoefficient(x_values,y_values)[1][0],4),".")

def DensityPlot_2(List1, List2, Label1, Label2, Title, AxisLabel):
    plt.figure()
    sns.distplot(List1, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'darkblue', rug = True, label = Label1)
    sns.distplot(List2, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'lightblue', rug = True, label = Label2)
    plt.title(Title)
    plt.xlabel(AxisLabel)
    plt.show()
    
def DensityPlot_3(List1, List2, List3, Label1, Label2, Label3, Title): 
    plt.figure()
    sns.distplot(List1, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'darkblue', rug = True, label = Label1)
    sns.distplot(List2, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'lightblue', rug = True, label = Label2)
    sns.distplot(List3, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'purple', rug = True, label = Label3)
    plt.title(Title)
    plt.xlabel("Birthweight (Grams)")
    plt.show()

def DensityPlot_4(List1, List2, List3, List4, Label1, Label2, Label3, Label4, Title): 
    plt.figure()
    sns.distplot(List1, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'darkblue', rug = True, label = Label1)
    sns.distplot(List2, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'lightblue', rug = True, label = Label2)
    sns.distplot(List3, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'purple', rug = True, label = Label3)
    sns.distplot(List4, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3}, color = 'lightgreen', rug = True, label = Label4)
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
    
#DESCRIPTIVE STATISTICS FUNCTIONS - individual variables
def mean_BW(List):
    mean = round(np.mean(List),1)
    return mean

def median_BW(List):
    median = round(np.median(List),1)
    return median

def stndDev_BW(List):
    if len(List) < 2:
        stndDev = "N/A"
    if len(List)>= 2:
        stndDev = round(statistics.stdev(List))
    return stndDev

def correlationCoefficient(x_values, y_values):
    return np.corrcoef(x_values, y_values)

def desStatsTable_2(ListAll, List1, List2, Label1, Label2, title, parameter):
    print("-------------------------------------------------------------------------------------")
    print("Data Table of Statistics: ", title)
    print("-------------------------------------------------------------------------------------")
    mothers = 'Number of Mothers', len(List1), len(List2), len(ListAll)
    means = 'Mean Birth Weight (grams)', mean_BW(List1), mean_BW(List2), mean_BW(ListAll)
    medians = 'Median Birth Weight (grams)', median_BW(List1), median_BW(List2), median_BW(ListAll)
    stndDevs = 'Standard Deviation (grams)', stndDev_BW(List1), stndDev_BW(List2), stndDev_BW(ListAll)
    data_rows = [mothers,means, medians, stndDevs]
    t = Table(rows = data_rows, names = (parameter,Label1, Label2, "All Datapoints"))
    print(t)

def desStatsTable_3(ListAll, List1, List2, List3, Label1, Label2, Label3, title, parameter):
    print("-------------------------------------------------------------------------------------")
    print("Data Table of Statistics: ", title)
    print("-------------------------------------------------------------------------------------")
    mothers = 'Number of Datapoints', len(List1), len(List2), len(List3), len(ListAll)
    means = 'Mean Birth Weight (grams)', mean_BW(List1), mean_BW(List2), mean_BW(List3), mean_BW(ListAll)
    medians = 'Median Birth Weight (grams)', median_BW(List1), median_BW(List2), median_BW(List3), median_BW(ListAll)
    stndDevs = 'Standard Deviation (grams)', stndDev_BW(List1), stndDev_BW(List2), stndDev_BW(List3), stndDev_BW(ListAll)
    data_rows = [mothers,means, medians, stndDevs]
    t = Table(rows = data_rows, names = (parameter,Label1, Label2, Label3, "All Datapoints"))
    print(t)
    
def desStatsTable_4(ListAll, List1, List2, List3, List4, Label1, Label2, Label3, Label4, title, parameter):
    print("-------------------------------------------------------------------------------------")
    print("Data Table of Statistics: ", title)
    print("-------------------------------------------------------------------------------------")
    mothers = 'Number of Datapoints', len(List1), len(List2), len(List3), len(List4), len(ListAll)
    means = 'Mean Birth Weight (grams)', mean_BW(List1), mean_BW(List2), mean_BW(List3), mean_BW(List4), mean_BW(ListAll)
    medians = 'Median Birth Weight (grams)', median_BW(List1), median_BW(List2), median_BW(List3), median_BW(List4), median_BW(ListAll)
    stndDevs = 'Standard Deviation (grams)', stndDev_BW(List1), stndDev_BW(List2), stndDev_BW(List3), stndDev_BW(List4), stndDev_BW(ListAll)
    data_rows = [mothers,means, medians, stndDevs]
    t = Table(rows = data_rows, names = (parameter, Label1, Label2, Label3, Label4, "All Datapoints"))
    print(t)
    
def desStatsTable_5(ListAll, List1, List2, List3, List4, List5, Label1, Label2, Label3, Label4, Label5, title, parameter):
    print("-------------------------------------------------------------------------------------")
    print("Data Table of Statistics: ", title)
    print("-------------------------------------------------------------------------------------")
    mothers = 'Number of Datapoints', len(List1), len(List2), len(List3), len(List4), len(List5), len(ListAll)
    means = 'Mean Birth Weight (grams)', mean_BW(List1), mean_BW(List2), mean_BW(List3), mean_BW(List4), mean_BW(List5), mean_BW(ListAll)
    medians = 'Median Birth Weight (grams)', median_BW(List1), median_BW(List2), median_BW(List3), median_BW(List4), median_BW(List5), median_BW(ListAll)
    stndDevs = 'Standard Deviation (grams)', stndDev_BW(List1), stndDev_BW(List2), stndDev_BW(List3), stndDev_BW(List4), stndDev_BW(List5), stndDev_BW(ListAll)
    data_rows = [mothers,means,medians,stndDevs]
    t = Table(rows = data_rows, names = (parameter,Label1, Label2, Label3, Label4, Label5, "All Datapoints"))
    print(t)
    
#TWO SAMPLE T-TEST FOR SAMPLES OF EQUAL SIZE
def T_test(List1, List2):
    p_value = stats.ttest_ind(List1, List2, axis = None, equal_var = False)[1]
    return p_value
    
def T_Test_Print(List1, List2, title): 
    print("-------------------------------------------------------------------------------------")
    print("T-test Results: ", title)
    print("-------------------------------------------------------------------------------------")
    p_value = T_test(List1, List2)
    if p_value <= 0.05:
        print("The two sample t-test on the two approximately normally distributed  curves returns a p-value of", round(p_value,5), ". This p-value confirms a statistically significant difference in the means of these two samples.")
    elif p_value > 0.05:
       print("The two sample t-test on the two approximately normally distributed curves returns a p-value of", round(p_value,5), ". This  p-value shows that the difference in the means of these two samples is not statistically significant.")
    else:
        print("The p-value for this data could not be determined as a result of sample size.")
    
def Chi_Square_Test(Array):
    chi2_stat, p_val, dof, ex = stats.chi2_contingency(Array)
    return p_val
    
def Chi_Square_Test_Print(Array, title, Variable1, Variable2):
    print("-------------------------------------------------------------------------------------")
    print("Chi-Square Test Results: ", title)
    print("-------------------------------------------------------------------------------------")
    chi2_stat, p_val, dof, ex = stats.chi2_contingency(Array)
    print("The Chi-Squre Test was preformed with", dof, "degrees of freedom.")
    if p_val < 0.05: 
        print("The Chi-Square Test on", Variable1, "and", Variable2, "returned a p-value of" ,round(p_val,5) , ". Therefore, these two variables are not independent of each other based and have a relationship based on the Chi-Square Test.")
    else: 
        print("The Chi-Square Test on", Variable1, "and", Variable2, "returned a p-value of" ,round(p_val,5), ". Therefore, these two variables are independent based on the Chi-Square Test.")
    
sigB = []
sigT = []
sigC = []
sigN = []
    
def Significance(Label,List1,List2,Array):
    if T_test(List1,List2) <= 0.05 and Chi_Square_Test(Array) <= 0.05:
        sigB.append(Label)
    elif T_test(List1,List2) <= 0.05:
        sigT.append(Label)
    elif Chi_Square_Test(Array) <= 0.05:
        sigC.append(Label)
    else:
        sigN.append(Label)

def Print_Significance():
    print("-------------------------------------------------------------------------------------")
    print("Significance")
    print("-------------------------------------------------------------------------------------")
    print("The variables that were found to be statistically significant in both the T-test and the Chi Square Test are:")
    print(sigB, '\n')
    print("The variables that were found to be statistically significant in the T-test but not the Chi Square Test are:")
    print(sigT, '\n')
    print("The variables that were found to be statistically significant in the Chi Square Test but not the T-Test are:")
    print(sigC, '\n')
    print("The variables that were found to be not statistically significant in both the T-test and the Chi Square Test are:")
    print(sigN, '\n')
    
def Effect(ListAll, Var1,List1,Var2, List2, Var3, List3, Var4, List4):
    print("-------------------------------------------------------------------------------------")
    print("Average Effect on Birthweight")
    print("-------------------------------------------------------------------------------------")
    print("Considering only the variables that were found to be statistically significant for both the T-test and the Chi Square Test,")
    avgChange1 = Var1, (round(mean_BW(List1) - mean_BW(ListAll),1))
    avgChange2 = Var2,(round(mean_BW(List2) - mean_BW(ListAll),1))
    avgChange3 = Var3,(round(mean_BW(List3) - mean_BW(ListAll),1))
    avgChange4 = Var4,(round(mean_BW(List4) - mean_BW(ListAll),1))
    datarows = [avgChange1,avgChange2,avgChange3,avgChange4]
    t = Table(rows = datarows, names = ('Variable','Average Change in Birthweight (grams)'))
    print(t)
    