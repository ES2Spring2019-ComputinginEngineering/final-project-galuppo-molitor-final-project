#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:12:14 2019

@author: victoriamolitor
"""
import csv 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


csv_file = open('Sample-Data-Birth-Weight-Risk.csv')
rows = sum(1 for row in csv_file) - 1
csv_file.seek(0)
csv_reader = csv.reader(csv_file, delimiter = ',')
Low_List = []
Low_Updated = []
Age = np.zeros((rows,))
LWT = np.zeros((rows,))
Smoker_List = []
Smoker_Updated = []
PTL = np.zeros((rows,))
Hypertension = np.zeros((rows,))
Hypertension_List = []
Hypertension_Updated = []
UI_List = []
UI_Updated = []
FTV = np.zeros((rows,))
BWT = np.zeros((rows,))
BWT_List = []

def readDataFile(): #This function parses data from a csv into numpy arrays. 
    Race = np.zeros((rows,))
    line_count = 0
    index = 0
    for row in csv_reader: 
        if line_count == 0:
            line_count += 1
        else:
            Low_List.append(row[1])
            Age[index] = row[2]
            LWT[index] = row[3]
            Race[index] = row[4]
            Smoker_List.append(row[5])
            PTL[index] = row[6]
            Hypertension_List.append(row[7])
            UI_List.append(row[8])
            FTV[index] = row[9]
            BWT[index] = row[10]
            BWT_List.append(row[10])
            index += 1
            line_count += 1
    for i in Low_List: #The categorical variables are parsed in as "TRUE" or "FALSE" and are converted to 0 and 1 in this for loop. 
        if i == 'FALSE': #False Low Birthweight values are labeled 0
            Low_Updated.append(0)
        else: #True Low Birthweight Values are labeled 1
            Low_Updated.append(1)
    for i in Smoker_List:
        if i == 'FALSE': #If the Mother is not a smoker, a value of 0 is stored
            Smoker_Updated.append(0)
        else: #If the Mother is a smoker, a value of 1 is stored
            Smoker_Updated.append(1) 
    for i in Hypertension_List: 
        if i == 'FALSE': #If the Mother does not have a history of hypertension, a value of 0 is stored
            Hypertension_Updated.append(0)
        else: #If the Mother has a history of hypertension, a value of 1 is stored
            Hypertension_Updated.append(1)
    for i in UI_List:
        if i == 'FALSE':
            UI_Updated.append(0) #if the mother has no history of uterine irritability, a value of 0 is stored
        else: 
            UI_Updated.append(1)#if the mother has a history of uterine irritability, a value of 1 is stored
    Low = np.array(Low_Updated)
    Smoker = np.array(Smoker_Updated)
    Hypertension = np.array(Hypertension_Updated)
    UI = np.array(UI_Updated)
    return Low, Age, LWT, Race, Smoker, PTL, Hypertension, UI, FTV, BWT #Arrays with data for each variabal are returned

#HISTOGRAM AND DENSITY PLOT DATA SEPARATION 
HypertensionPos_BW = []
HypertensionNeg_BW = []
Smoker_Birthweights = []
NonSmoker_Birthweights = []
UINeg = []
UIPos = []
Low_BW = []
Normal_BW = []
All_Birthweights = []
Low_Ages = []
Normal_Ages = []
Low_NW = []
Normal_NW = []

def List_Creation1(List1, Input): #Takes in an array as Input and returns a list with the same values
    List1 = np.array(Input).tolist()
    return List1

def List_Creation2(List1, List2, Input, Paramater): #Takes in an array as Input1 and returns two lists with values separated based on the categorical factor and the paramater. 
    Input_List = np.array(Input).tolist()
    for i in range(189): 
        if Input_List[i] == 0: 
            List1.append(Paramater[i]) #In this case, the paramater used was birth weight, and these values are separated based on a category. 
        else: 
            List2.append(Paramater[i])
    return List1, List2

Race_1 = []
Race_2 = []
Race_3 = []
#List_Creation3, List_Creation4, and List_Creation5 create the same lists for variables with a different number of categories.
def List_Creation3(List1, List2, List3, Input, Paramater):
    Input_List = np.array(Input).tolist()
    for i in range(189):
        if Input_List[i] == 1:
            List1.append(Paramater[i])
        elif Input_List[i] == 2: 
            List2.append(Paramater[i])
        else:
            List3.append(Paramater[i])
    return List1, List2, List3
    
PTL_0 = []
PTL_1 = []
PTL_2 = []
PTL_3 = []

def List_Creation4(List1, List2, List3, List4, Input, Paramater): 
    Low, Age, LWT, Race, Smoker, PTL, Hypertension, UI, FTV, BWT = readDataFile()
    Input_List = np.array(Input).tolist()
    for i in range(189):
        if Input_List[i] == 0:
            List1.append(Paramater[i])
        elif Input_List[i] == 1:
            List2.append(Paramater[i])
        elif Input_List[i] == 2:
            List3.append(Paramater[i])
        else:
            List4.append(Paramater[i])
    return List1, List2, List3, List4 

FTV_0 = []
FTV_1 = []
FTV_2 = []
FTV_3 = []
FTV_4 = [] 

def List_Creation5(List1, List2, List3, List4, List5, Input, Paramater): 
    Input_List = np.array(Input).tolist()
    for i in range(189):
        if Input_List[i] == 0: 
            List1.append(Paramater[i])
        elif Input_List[i] == 1:
            List2.append(Paramater[i])
        elif Input_List[i] == 2: 
            List3.append(Paramater[i])
        elif Input_List[i] == 3: 
            List4.append(Paramater[i])
        else: 
            List5.append(Paramater[i])
    return(List1, List2, List3, List4, List5)

#CREATION OF ARRAYS FOR CHI-SQUARE TESTS
def Chi_Square_2(Array1, Array2): #Chi_Square_2 takes in two arrays and counts the number of subjects in each category. 
    Count1 = 0
    Count2 = 0
    Count3 = 0
    Count4 = 0
    List1 = np.array(Array1).tolist() #Ex: List 1 is variable 1
    List2 = np.array(Array2).tolist() #Ex: List 2 is variable 2
    for i in range(189):
        if List1[i] == 0 and List2[i] == 0: #Ex: Negative for Variables 1 and 2
            Count1 += 1
        elif List1[i] == 0 and List2[i] == 1: #Ex: Negative for Variable 1, Positive for Variable 2
            Count2 += 1
        elif List1[i] == 1 and List2[i] == 0: #Ex: Positive for Variable 1, Negative for Variable 2
            Count3 += 1
        else: #Ex: Positive for Variables 1 and 2
            Count4 += 1
    a1 = [Count1, Count2]
    a2 = [Count3, Count4]
    Chi_Square_Array = np.array([a1,a2]) #Combines the two lists into an array which can be used for the Chi-Square test
    return Chi_Square_Array

#Chi_Square_3, Chi_Square_4, and Chi_Square 5 create arrays for more categories. 
def Chi_Square_3(Array1, Array2): 
    Count1 = 0
    Count2 = 0
    Count3 = 0
    Count4 = 0
    Count5 = 0
    Count6 = 0
    List1 = np.array(Array1).tolist()
    List2 = np.array(Array2).tolist()
    for i in range(189):
        if List1[i] == 0 and List2[i]==1:
            Count1 += 1
        elif List1[i] == 0 and List2[i]==2:
            Count2 += 1
        elif List1[i] == 0 and List2[i]==3: 
            Count3 += 1
        elif List1[i] == 1 and List2[i]==1:
            Count4 += 1
        elif List1[i] == 1 and List2[i]==2:
            Count5 += 1
        else:
            Count6 += 1
    a1 = [Count1, Count2, Count3]
    a2 = [Count4, Count5, Count6]
    Chi_Square_Array = np.array([a1,a2])
    return Chi_Square_Array

def Chi_Square_4(Array1, Array2): 
    Count1 = 0
    Count2 = 0
    Count3 = 0
    Count4 = 0
    Count5 = 0
    Count6 = 0
    Count7 = 0
    Count8 = 0
    List1 = np.array(Array1).tolist()
    List2 = np.array(Array2).tolist()
    for i in range(189):
        if List1[i] == 0 and List2[i]==0:
            Count1 += 1
        elif List1[i] == 0 and List2[i]==1:
            Count2 += 1
        elif List1[i] == 0 and List2[i]==2: 
            Count3 += 1
        elif List1[i] == 0 and List2[i]==3: 
            Count4 += 1
        elif List1[i] == 1 and List2[i]==0:
            Count5 += 1
        elif List1[i] == 1 and List2[i]==1:
            Count6 += 1
        elif List1[i] == 1 and List2[i]==2: 
            Count7 += 1
        else:
            Count8 += 1
    a1 = [Count1, Count2, Count3, Count4]
    a2 = [Count5, Count6, Count7, Count8]
    Chi_Square_Array = np.array([a1,a2])
    return Chi_Square_Array

def Chi_Square_5(Array1, Array2): 
    Count1 = 0
    Count2 = 0
    Count3 = 0
    Count4 = 0
    Count5 = 0
    Count6 = 0
    Count7 = 0
    Count8 = 0
    Count9 = 0
    Count10 = 0
    List1 = np.array(Array1).tolist()
    List2 = np.array(Array2).tolist()
    for i in range(189):
        if List1[i] == 0 and List2[i]==0:
            Count1 += 1
        elif List1[i] == 0 and List2[i]==1:
            Count2 += 1
        elif List1[i] == 0 and List2[i]==2: 
            Count3 += 1
        elif List1[i] == 0 and List2[i]==3: 
            Count4 += 1
        elif List1[i] == 0 and List2[i] ==4: 
            Count5 += 1
        elif List1[i] == 1 and List2[i]==0:
            Count6 += 1
        elif List1[i] == 1 and List2[i]==1:
            Count7 += 1
        elif List1[i] == 1 and List2[i]==2: 
            Count8 += 1
        elif List1[i] == 1 and List2[i]==3:
            Count9 += 1
        else:
            Count10 += 1
    a1 = [Count1, Count2, Count3, Count4, Count5]
    a2 = [Count6, Count7, Count8, Count9, Count10]
    Chi_Square_Array = np.array([a1,a2])
    return Chi_Square_Array

Neg_UI_Neg_S = []
Neg_UI_Pos_S = []
Pos_UI_Neg_S = []
Pos_UI_Pos_S = []

Neg_H_Neg_S = []
Neg_H_Pos_S = []
Pos_H_Neg_S = []
Pos_H_Pos_S = []

Neg_UI_Neg_H = []
Neg_UI_Pos_H = []
Pos_UI_Neg_H = []
Pos_UI_Pos_H = []

#Multi_Factor separates two input arrays into four lists based on data from two categories. 
def Multi_Factor(List1, List2, List3, List4, Input1, Input2, Paramater):
    Input1_List = np.array(Input1).tolist()
    Input2_List = np.array(Input2).tolist()
    for i in range(189): 
        if Input1_List[i] == 0 and Input2_List[i] == 0: 
            List1.append(Paramater[i])
        elif Input1_List[i] == 0 and Input2_List[i] == 1:
            List2.append(Paramater[i])
        elif Input1_List[i] == 1 and Input2_List[i] == 0:
            List3.append(Paramater[i])
        else:
            List4.append(Paramater[i])
    return List1, List2, List3, List4
