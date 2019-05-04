"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# IMPORT STATEMENTS
import numpy as np
import csv
import matplotlib.pyplot as plt
from DataParsing import * #wrong way to import?
from Functions import * #wrong way to import?


# DEMONSTRATION CODE
titlePrint("There are eight different variables to be considered as factors observed in this dataset that may have an effect on the chances of a low birth weight. The individual correlation between birth weight and each of the 9 variables is demonstrated in the following:")

titlePrint("Age of Mother")
graphNumerical(Age, BWT, Low, 'Graph of Age on Birth Weight')

titlePrint("Normal Weight of Mother")
graphNumerical(LWT, BWT, Low, 'Graph of Normal Weight of Mother on Birth Weight')

titlePrint("Smoking During Pregnancy")
DensityPlot_2(NonSmoker_Birthweights, Smoker_Birthweights, 'Non-Smokers', 'Smokers', 'Density Curve: Smoking During Pregnancy')
desStatsTable_2(BWT, NonSmoker_Birthweights, Smoker_Birthweights, 'Non-Smokers', 'Smokers','Smoking During Pregnancy', 'Smoking Status')
T_Test_Print(NonSmoker_Birthweights, Smoker_Birthweights, 'Smoking During Pregnancy')
Chi_Square_Test_Print(Smoker_Low, "Low Birthweight and Smoking", "Low Birthweight", "Smoking")
Significance("Smoking During Pregnancy",NonSmoker_Birthweights, Smoker_Birthweights,Smoker_Low)

titlePrint("Medical History of Hypertension")
DensityPlot_2(HypertensionNeg_BW, HypertensionPos_BW, 'No History of Hypertension', 'History of Hypertension', 'Density Curve: Hypertension Birthweights')
desStatsTable_2(BWT, HypertensionNeg_BW, HypertensionPos_BW, 'Negative', 'Positive','Hypertension', 'History of Hypertension')
T_Test_Print(HypertensionNeg_BW, HypertensionPos_BW,'Hypertension')
Chi_Square_Test_Print(Hypertension_Low, "Low Birthweight and Hypertension", "Low Birthweight", "Hypertension")
Significance("Medical History of Hypertension",HypertensionNeg_BW, HypertensionPos_BW,Hypertension_Low)

titlePrint("Uterine Irritability")
DensityPlot_2(UIPos, UINeg, 'History of Uterine Irritability', 'No History of Uterine Irratibility', 'Density Curve: Uterine Irratibility Birthweights')
desStatsTable_2(BWT, UIPos, UINeg, 'Positive', 'Negative', 'Uterine Irratibility', 'History of Uterine Irritability')
T_Test_Print(UINeg, UIPos, 'Uterine Irratibility')
Chi_Square_Test_Print(UI_Low, "Low Birthweight and Uterine Irritability", "Low Birthweight", "Uterine Irritability")
Significance("Uterine Irritability",UINeg, UIPos,UI_Low)

titlePrint("Race of Mother")
DensityPlot_3(Race_1, Race_2, Race_3, 'Race 1', 'Race 2', 'Race 3', 'Density Curve: Race of Mother')
desStatsTable_3(BWT, Race_1, Race_2, Race_3, '1', '2', '3','Race of Mother', 'Race')
T_Test_Print(Race_1, Race_2+Race_3, 'Race of Mother (Race 1)')
T_Test_Print(Race_2, Race_1+Race_3, 'Race of Mother (Race 2)')
T_Test_Print(Race_3, Race_1+Race_2, 'Race of Mother (Race 3)')
Chi_Square_Test_Print(Race_Low, "Low Birthweight and Race of Mother", "Low Birthweight", "Race of Mother")
Significance("Race of Mother: Race 1",Race_1, Race_2+Race_3,Race_Low)
Significance("Race of Mother: Race 2",Race_2, Race_1+Race_3,Race_Low)
Significance("Race of Mother: Race 3",Race_3, Race_1+Race_2,Race_Low)

titlePrint("Number of Premature Births in Medical History")
DensityPlot_4(PTL_0, PTL_1, PTL_2, PTL_3, '0 Premature Births', '1 Premature Birth', '2 Premature Births', '3 Premature Births', 'Density Curve: Number of Premature Births in Medical History')
desStatsTable_4(BWT, PTL_0, PTL_1, PTL_2, PTL_3, '0', '1', '2', '3', 'Number of Premature Births in Medical History', 'Premature Births')
T_Test_Print(PTL_0, PTL_1+PTL_2+PTL_3, '0 Premature Births')
T_Test_Print(PTL_1, PTL_0+PTL_2+PTL_3, '1 Premature Birth')
T_Test_Print(PTL_2, PTL_0+PTL_1+PTL_3, '2 Premature Births')
T_Test_Print(PTL_3, PTL_0+PTL_1+PTL_2, '3 Premature Births')
Chi_Square_Test_Print(PTL_Low, "Low Birthweight and Number of Premature Births in Medical History", "Low Birthweight", "Number of Premature Births")
Significance("No Premature Births in Medical History",PTL_0, PTL_1+PTL_2+PTL_3,PTL_Low)
Significance("One Premature Births in Medical History",PTL_1, PTL_0+PTL_2+PTL_3,PTL_Low)
Significance("Two Premature Births in Medical History",PTL_2, PTL_0+PTL_1+PTL_3,PTL_Low)
Significance("Three Premature Births in Medical History",PTL_3, PTL_0+PTL_1+PTL_2,PTL_Low)

titlePrint("Number of Medical Consultations During First Trimester")
DensityPlot_5(FTV_0, FTV_1, FTV_2, FTV_3, FTV_4, '0 Visits', '1 Visit', '2 Visits', '3 Visits', '4 Visits', 'Density Curve:Number of Medical Consultations During First Trimester' )
desStatsTable_5(BWT, FTV_0, FTV_1, FTV_2, FTV_3, FTV_4, '0', '1', '2', '3', '4', 'Number of Medical Consultations During First Trimester', 'Number of Visits')
T_Test_Print(FTV_0, FTV_1+FTV_2+FTV_3+FTV_4, '0 Medical Consultations During First Trimester')
T_Test_Print(FTV_1, FTV_0+FTV_2+FTV_3+FTV_4, '1 Medical Consultation During First Trimester')
T_Test_Print(FTV_2, FTV_1+FTV_0+FTV_3+FTV_4, '2 Medical Consultations During First Trimester')
T_Test_Print(FTV_3, FTV_1+FTV_2+FTV_0+FTV_4, '3 Medical Consultations During First Trimester')
T_Test_Print(FTV_4, FTV_1+FTV_2+FTV_3+FTV_0, '4 Medical Consultations During First Trimester')
Chi_Square_Test_Print(FTV_Low, "Low Birthweight and Number of Medical Consultations During First Trimester", "Low Birthweight", "Number of Medical Consultations During First Trimester")
Significance("No Medical Consultations During First Trimester",FTV_0, FTV_1+FTV_2+FTV_3+FTV_4,FTV_Low)
Significance("One Medical Consultations During First Trimester",FTV_1, FTV_0+FTV_2+FTV_3+FTV_4,FTV_Low)
Significance("Two Medical Consultations During First Trimester",FTV_2, FTV_1+FTV_0+FTV_3+FTV_4,FTV_Low)
Significance("Three Medical Consultations During First Trimester",FTV_3, FTV_1+FTV_2+FTV_0+FTV_4,FTV_Low)
Significance("Four Medical Consultations During First Trimester",FTV_4, FTV_1+FTV_2+FTV_3+FTV_0,FTV_Low)

titlePrint("Summary of Variable Effect on Birthweight")
Print_Significance()
Effect(BWT,'Smoking During Pregnancy',Smoker_Birthweights,'Uterine Irritability', UIPos, 'No Premature Births in Medical History', PTL_0, 'One Premature Birth in Medical History', PTL_1)

###############################################################################################
#
#titlePrint("Comparisons of Multiple Factors")
#titlePrint("Uterine Irratibility and Smoking During Pregnancy")
#DensityPlot_4(Neg_UI_Neg_S, Neg_UI_Pos_S, Pos_UI_Neg_S, Pos_UI_Pos_S, 'No History of UI, Non-Smoker', 'No History of UI, Smoker', 'History of UI, Non-Smoker', 'History of UI, Smoker', 'Uterine Irratibility and Smoking')
#desStatsTable_4(BWT,Neg_UI_Neg_S, Neg_UI_Pos_S, Pos_UI_Neg_S, Pos_UI_Pos_S, 'Neg/Neg', 'Neg/Pos', 'Pos/Neg', 'Pos/Pos', 'Uterine Irratibility and Smoking', 'UI and Smoking')
#T_Test_Print(Neg_UI_Pos_S, Neg_UI_Neg_S, 'No History of Uterine Irratibiility, Smoker during Pregnancy')
#T_Test_Print(Pos_UI_Neg_S, Neg_UI_Neg_S, 'History of Uterine Irratibiility, Non-Smoker during Pregnancy')
#T_Test_Print(Pos_UI_Pos_S, Neg_UI_Neg_S, 'History of Uterine Irratibiility, Smoker during Pregnancy')
#
#titlePrint("Hypertension and Smoking During Pregnancy")
#DensityPlot_4(Neg_H_Neg_S, Neg_H_Pos_S, Pos_H_Neg_S, Pos_H_Pos_S, 'No History of Hypertension, Non-Smoker', 'No History of Hypertension, Smoker', 'History of Hypertension, Non-Smoker', 'History of Hypertension, Smoker', 'History of Hypertension and Smoking During Pregnancy')
#desStatsTable_4(BWT, Neg_H_Neg_S, Neg_H_Pos_S, Pos_H_Neg_S, Pos_H_Pos_S, 'Neg/Neg', 'Neg/Pos', 'Pos/Neg', 'Pos/Pos', 'History of Hypertension and Smoking During Pregnancy', 'Hypertesion and Smoking')
#T_Test_Print(Neg_H_Pos_S, Neg_H_Neg_S, 'No History of Hypertension, Smoker During Pregnancy')
#T_Test_Print(Pos_H_Neg_S, Neg_H_Neg_S, 'History of Hypertension, Non-Smoker During Pregnancy')
#T_Test_Print(Pos_H_Pos_S, Neg_H_Neg_S, 'History of Hypertension, Smoker During Pregnancy')
#
#titlePrint("Uterine Irritability and History of Hypertension")
#DensityPlot_4(Neg_UI_Neg_H, Neg_UI_Pos_H, Pos_UI_Neg_H, Pos_UI_Pos_H, 'No History of UI or Hypertension', 'No History of UI, History of Hypertension', 'History of UI, No History of Hypertension', 'History of UI and Hypertension', 'History of Hypertension and Uterine Irritability')
#desStatsTable_4(BWT, Neg_UI_Neg_H, Neg_UI_Pos_H, Pos_UI_Neg_H, Pos_UI_Pos_H,'Neg/Neg', 'Neg/Pos', 'Pos/Neg', 'Pos/Pos', 'History of Hypertension and Uterine Irritability', 'Uterine Irritability and Smoking')
#T_Test_Print(Neg_UI_Pos_H, Neg_UI_Neg_H, 'No History of Uterine Irritability, History of Hypertension')
#T_Test_Print(Pos_UI_Neg_H, Neg_UI_Neg_H, 'History of Uterine Irritability, No Hisitory of Hypertension')
#T_Test_Print(Pos_UI_Pos_H, Neg_UI_Neg_H, 'History of Uterine Irritabiility and Hypertension')