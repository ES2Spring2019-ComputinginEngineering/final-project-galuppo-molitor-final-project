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

def graphData(x_values, y_values, classification, title): 
    
    plt.figure
    plt.plot(x_values[classification == 0], y_values[classification == 0], "b.", label = 'Class 0: Normal Birth Weight')
    plt.plot(x_values[classification == 1], y_values[classification == 1], "r.", label = 'Class 1: Low Birth Weight')
    plt.legend()
    plt.show()


# DEMONSTRATION CODE
print("There are nine different risk factors observed in this dataset that may have an effect on the chances of a low birth weight")
print("The individual correlation between birth weight and each the 9 risk factors is demonstrated in the following:")
graphData(Age, BWT, Low, 'Graph of Age on Birth Weight')
linearFit(Age, BWT)
linearFit_Conditions(Age, BWT, Low)



