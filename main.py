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
print("There are nine different risk factors observed in this dataset that may have an effect on the chances of a low birth weight")
print('\n', "The individual correlation between birth weight and each the 9 risk factors is demonstrated in the following:")

print('\n','\n', "NUMERICAL RISKS as scatter plots")
print('\n', "Age of Mother")
graphNumerical(Age, BWT, Low, 'Graph of Age on Birth Weight')
print(correlationCoefficient(Age, BWT))
print('\n', "Normal Weight of Mother")
graphNumerical(LWT, BWT, Low, 'Graph of Normal Weight of Mother on Birth Weight')

print('\n', "Number of Premature Births in Medical History")
#graphNumerical(PTL, BWT, Low, 'Graph of Number of Premature Births in Medical History on Birth Weight')


print('\n', "Number of Medical Consultations During First Trimester")
#graphNumerical(FTV, BWT, Low, 'Graph of Number of Medical Consultations During First Trimester on Birth Weight')
desStatsTable_5(BWT, FTV_0, FTV_1, FTV_2, FTV_3, FTV_4, '0 Visits', '1 Visit', '2 Visits', '3 Visits', '4 Visits', 'Data Table of Statistics: Number of Medical Consultations During First Trimester')
DensityPlot_5(FTV_0, FTV_1, FTV_2, FTV_3, FTV_4, '0 Visits', '1 Visit', '2 Visits', '3 Visits', '4 Visits', 'Density Curve:Number of Medical Consultations During First Trimester' )

#graphCategorical(LWT, BWT, Low, "Title")
print('\n', "Race of Mother")
desStatsTable_3(BWT, Race_1, Race_2, Race_3, 'Race 1', 'Race 2', 'Race 3','Data Table of Statistics: Race of Mother')
DensityPlot_3(Race_1, Race_2, Race_3, 'Race 1', 'Race 2', 'Race 3', 'Density Curve: Race of Mother')

print('\n', "Smoking During Pregnancy")
#Histogram_2(NonSmoker_Birthweights, Smoker_Birthweights, ['Non-Smoker Birthweights', 'Smoker Birthweights'], 8)
desStatsTable_2(BWT, NonSmoker_Birthweights, Smoker_Birthweights, 'Non-Smokers', 'Smokers','Data Table of Statistics: Smoking During Pregnancy')
DensityPlot_2(NonSmoker_Birthweights, Smoker_Birthweights, 'Non-Smokers', 'Smokers', 'Density Curve: Smoking During Pregnancy')

print('\n', "Medical History of Hypertension")
desStatsTable_2(BWT, HypertensionNeg_BW, HypertensionPos_BW, 'No History of Hypertension', 'History of Hypertension','Data Table of Statistics: Hypertension Risk Factor')
DensityPlot_2(HypertensionNeg_BW, HypertensionPos_BW, 'No History of Hypertension', 'History of Hypertension', 'Density Curve: Hypertension Birthweights')

print('\n', "Uterine Irritability")
desStatsTable_2(BWT, UIPos, UINeg, 'History of Uterine Irritability', 'No History of Uterine Irratibility', 'Data Table of Statistics: Uterine Irratibility Risk Factor')
DensityPlot_2(UIPos, UINeg, 'History of Uterine Irritability', 'No History of Uterine Irratibility', 'Density Curve: Uterine Irratibility Birthweights')