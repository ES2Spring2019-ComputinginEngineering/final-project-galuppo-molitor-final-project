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

def readDataFile():
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
    for i in Low_List: 
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
        if i == 'FALSE': #If the Mother does not have Hypertension, a value of 0 is stored
            Hypertension_Updated.append(0)
        else: #If the Mother has Hypertension, a value of 1 is stored
            Hypertension_Updated.append(1)
    for i in UI_List:
        if i == 'FALSE':
            UI_Updated.append(0)
        else: 
            UI_Updated.append(1)
    Low = np.array(Low_Updated)
    Smoker = np.array(Smoker_Updated)
    Hypertension = np.array(Hypertension_Updated)
    UI = np.array(UI_Updated)
    return Low, Age, LWT, Race, Smoker, PTL, Hypertension, UI, FTV, BWT 

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

def List_Creation1(List1, Input): 
    List1 = np.array(Input).tolist()
    return List1

def List_Creation2(List1, List2, Input): 
    Input_List = np.array(Input).tolist()
    for i in range(189): 
        if Input_List[i] == 0: 
            List1.append(BWT[i])
        else: 
            List2.append(BWT[i])
    return List1, List2

Race_1 = []
Race_2 = []
Race_3 = []
def List_Creation3(List1, List2, List3, Input):
    Low, Age, LWT, Race, Smoker, PTL, Hypertension, UI, FTV, BWT = readDataFile()
    Input_List = np.array(Input).tolist()
    for i in range(189):
        if Input_List[i] == 1:
            List1.append(BWT[i])
        elif Input_List[i] == 2: 
            List2.append(BWT[i])
        else:
            List3.append(BWT[i])
    return List1, List2, List3
    
PTL_0 = []
PTL_1 = []
PTL_2 = []
PTL_3 = []

def List_Creation4(List1, List2, List3, List4, Input): 
    Low, Age, LWT, Race, Smoker, PTL, Hypertension, UI, FTV, BWT = readDataFile()
    Input_List = np.array(Input).tolist()
    for i in range(189):
        if Input_List[i] == 0:
            List1.append(BWT[i])
        elif Input_List[i] == 1:
            List2.append(BWT[i])
        elif Input_List[i] == 2:
            List3.append(BWT[i])
        else:
            List4.append(BWT[i])
    return List1, List2, List3, List4 

FTV_0 = []
FTV_1 = []
FTV_2 = []
FTV_3 = []
FTV_4 = [] 

def List_Creation5(List1, List2, List3, List4, List5, Input): 
    Low, Age, LWT, Race, Smoker, PTL, Hypertension, UI, FTV, BWT = readDataFile()
    Input_List = np.array(Input).tolist()
    for i in range(189):
        if Input_List[i] == 0: 
            List1.append(BWT[i])
        elif Input_List[i] == 1:
            List2.append(BWT[i])
        elif Input_List[i] == 2: 
            List3.append(BWT[i])
        elif Input_List[i] == 3: 
            List4.append(BWT[i])
        else: 
            List5.append(BWT[i])
    return(List1, List2, List3, List4, List5)
    
