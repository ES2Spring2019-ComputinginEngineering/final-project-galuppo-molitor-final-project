#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:12:14 2019

@author: victoriamolitor
"""
import csv 
import numpy as np
import matplotlib.pyplot as plt

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
