"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import numpy as np
import csv
import matplotlib.pyplot as plt
from DataParsing import * 
from Functions import *


# DEMONSTRATION CODE
print("There are nine different risk factors observed in this dataset that may have an effect on the chances of a low birth weight")
print('\n', "The individual correlation between birth weight and each the 9 risk factors is demonstrated in the following:")

print('\n','\n', "NUMERICAL RISKS as scatter plots")
print('\n', "Age of Mother")
graphAll(Age, BWT, Low, 'Graph of Age on Birth Weight')
print(correlationCoeddicient(Age, BWT))
print('\n', "Normal Weight of Mother")
graphAll(LWT, BWT, Low, 'Graph of Normal Weight of Mother on Birth Weight')

print('\n', "????")
print('\n', "Number of Premature Births in Medical History")
graphAll(PTL, BWT, Low, 'Graph of Number of Premature Births in Medical History on Birth Weight')
print('\n', "Number of Medical Consultations During First Trimester")
graphAll(FTV, BWT, Low, 'Graph of Number of Medical Consultations During First Trimester on Birth Weight')

print('\n', "CATEGORICAL RISKS as histograms")
#print('\n', "Race of Mother")
#graphAll(Race, BWT, Low, 'Graph of Race of Mother on Birth Weight')
#print('\n', "Smoking During Pregnancy")
#graphAll(Smoker, BWT, Low, 'Graph of Smoking During Pregnancy on Birth Weight')
#print('\n', "Medical History of Hypertension")
#graphAll(Hypertension, BWT, Low, 'Graph of Medical History of Hypertension on Birth Weight')
#print('\n', "Uterine Irritability")
#graphAll(UI, BWT, Low, 'Graph of Uterine Irritability on Birth Weight')
