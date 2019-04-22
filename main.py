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
graphNumerical(Age, BWT, Low, 'Graph of Age on Birth Weight')
print(correlationCoefficient(Age, BWT))
print('\n', "Normal Weight of Mother")
graphNumerical(LWT, BWT, Low, 'Graph of Normal Weight of Mother on Birth Weight')

print('\n', "Number of Premature Births in Medical History")
graphNumerical(PTL, BWT, Low, 'Graph of Number of Premature Births in Medical History on Birth Weight')
print('\n', "Number of Medical Consultations During First Trimester")
graphNumerical(FTV, BWT, Low, 'Graph of Number of Medical Consultations During First Trimester on Birth Weight')
DensityPlot_5(FTV_0, FTV_1, FTV_2, FTV_3, FTV_4, '0 Visits', '1 Visit', '2 Visits', '3 Visits', '4 Visits', 'Density Curve:Number of Medical Consultations During First Trimester' )

print('\n', "CATEGORICAL RISKS as histograms")
#graphCategorical(LWT, BWT, Low, "Title")
print('\n', "Race of Mother")
print("The mean birth weight among mothers in Race 1 is", round(sum(Race_1)/len(Race_1),1), 'grams. The mean birthweight for Race 2 is', round(sum(Race_2)/len(Race_2),2), 'grams. The mean birthweight for Race 3 is', round(sum(Race_3)/len(Race_3),1))
DensityPlot_3(Race_1, Race_2, Race_3, 'Race 1', 'Race 2', 'Race 3', 'Density Curve: Race of Mother')


#graphAll(Race, BWT, Low, 'Graph of Race of Mother on Birth Weight')
print('\n', "Smoking During Pregnancy")
#Histogram_2(NonSmoker_Birthweights, Smoker_Birthweights, ['Non-Smoker Birthweights', 'Smoker Birthweights'], 8)
print("The mean birth weight among smokers is", round(sum(Smoker_Birthweights)/len(Smoker_Birthweights),1), 'grams. The mean birthweight among non-smokers is', round(sum(NonSmoker_Birthweights)/len(NonSmoker_Birthweights),1), 'grams.')
DensityPlot_2(NonSmoker_Birthweights, Smoker_Birthweights, 'Non-Smokers', 'Smokers', 'Density Curve: Smoking During Pregnancy')

print('\n', "Medical History of Hypertension")
print("The mean birth weight among mothers with a history of Hypertension is", round(sum(HypertensionPos_BW)/len(HypertensionPos_BW),1), 'grams. The mean birthweight among those without a history of Hypertension is', round(sum(HypertensionNeg_BW)/len(HypertensionNeg_BW),1), 'grams.')
print("There were", len(HypertensionPos_BW), "mothers with a history of hypertension, and", len(HypertensionNeg_BW), "without a history of hypertension.")
DensityPlot_2(HypertensionNeg_BW, HypertensionPos_BW, 'No History of Hypertension', 'History of Hypertension', 'Density Curve: Hypertension Birthweights')

print('\n', "Uterine Irritability")
print("The mean birth weight among mothers with a history of Uterine Irritability is", round(sum(UIPos)/len(UIPos),1), "grams. The mean birthweight among those without a history of Uterine Irratibility is", round(sum(UINeg)/len(UINeg),1),'grams.')
DensityPlot_2(UIPos, UINeg, 'History of Uterine Irritability', 'No History of Uterine Irratibility', 'Density Curve: Uterine Irratibility Birthweights')
#graphAll(UI, BWT, Low, 'Graph of Uterine Irritability on Birth Weight')