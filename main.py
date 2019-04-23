"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import numpy as np
import csv
import matplotlib.pyplot as plt
from DataParsing import * #wrong way to import?
from Functions import * #wrong way to import?


# DEMONSTRATION CODE
print("There are eight different risk factors observed in this dataset that may have an effect on the chances of a low birth weight")
print('\n', "The individual correlation between birth weight and each the 9 risk factors is demonstrated in the following:")

titlePrint("Age of Mother")
graphNumerical(Age, BWT, Low, 'Graph of Age on Birth Weight')

titlePrint("Normal Weight of Mother")
graphNumerical(LWT, BWT, Low, 'Graph of Normal Weight of Mother on Birth Weight')

titlePrint("Smoking During Pregnancy")
#Histogram_2(NonSmoker_Birthweights, Smoker_Birthweights, ['Non-Smoker Birthweights', 'Smoker Birthweights'], 8)
desStatsTable_2(BWT, NonSmoker_Birthweights, Smoker_Birthweights, 'Non-Smokers', 'Smokers','Smoking During Pregnancy', 'Smoking Status')
DensityPlot_2(NonSmoker_Birthweights, Smoker_Birthweights, 'Non-Smokers', 'Smokers', 'Density Curve: Smoking During Pregnancy')
T_Test_Print(NonSmoker_Birthweights, Smoker_Birthweights)

titlePrint("Medical History of Hypertension")
desStatsTable_2(BWT, HypertensionNeg_BW, HypertensionPos_BW, 'Negative', 'Positive','Hypertension Risk Factor', 'History of Hypertension')
DensityPlot_2(HypertensionNeg_BW, HypertensionPos_BW, 'No History of Hypertension', 'History of Hypertension', 'Density Curve: Hypertension Birthweights')
T_Test_Print(HypertensionNeg_BW, HypertensionPos_BW)

titlePrint("Uterine Irritability")
desStatsTable_2(BWT, UIPos, UINeg, 'Positive', 'Negative', 'Uterine Irratibility Risk Factor', 'History of Uterine Irritability')
DensityPlot_2(UIPos, UINeg, 'History of Uterine Irritability', 'No History of Uterine Irratibility', 'Density Curve: Uterine Irratibility Birthweights')
T_Test_Print(UINeg, UIPos)

titlePrint("Race of Mother")
desStatsTable_3(BWT, Race_1, Race_2, Race_3, '1', '2', '3','Race of Mother', 'Race')
DensityPlot_3(Race_1, Race_2, Race_3, 'Race 1', 'Race 2', 'Race 3', 'Density Curve: Race of Mother')
print("For Race 1:")
T_Test_Print(Race_1, Race_2+Race_3)
print("For Race 2:")
T_Test_Print(Race_2, Race_1+Race_3)
print("For Race 3:")
T_Test_Print(Race_3, Race_1+Race_2)

titlePrint("Number of Premature Births in Medical History")
desStatsTable_4(BWT, PTL_0, PTL_1, PTL_2, PTL_3, '0', '1', '2', '3', 'Number of Premature Births in Medical History', 'Premature Births')
DensityPlot_4(PTL_0, PTL_1, PTL_2, PTL_3, '0 Premature Births', '1 Premature Birth', '2 Premature Births', '3 Premature Births', 'Density Curve: Number of Premature Births in Medical History')

titlePrint("Number of Medical Consultations During First Trimester")
desStatsTable_5(BWT, FTV_0, FTV_1, FTV_2, FTV_3, FTV_4, '0', '1', '2', '3', '4', 'Number of Medical Consultations During First Trimester', 'Number of Visits')
DensityPlot_5(FTV_0, FTV_1, FTV_2, FTV_3, FTV_4, '0 Visits', '1 Visit', '2 Visits', '3 Visits', '4 Visits', 'Density Curve:Number of Medical Consultations During First Trimester' )
