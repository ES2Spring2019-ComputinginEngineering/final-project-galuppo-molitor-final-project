# This is your Final Project ReadMe Template

The file is inside your final project repository called "README.md"

You should include in your final project readme a description of the project, a list of all the files that you have created and instructions for use.

This readme is written in a language called markdown. This is not a programming language but a formatting langauge. There are symbols (syntax) used to indicate how to format the text. For example the pound symbol (i.e. the hashtag) is used to format a title; two of the same symbol format a heading, and three format a sub-heading.

Below is some example text in markdown however this alone is not suffiecent for the final project. **Make sure you follow the directions on Canvas.**

Delete the instructions above this line and the line:

---------------------------------------------

# Project Title

Short project description here, click the **EDIT (pencil) button** in the top right corner of this frame to copy the markdown formatted template.

## Instructions

Describe how the users(instructors) should run your code to see an ***easy to run example of the functionality***. This should all be in a *main.py* "driver" script.

## File List

Create a list of all of the files in your repository with one sentence descriptions 

## How to format your readme

In your readme, you can:
```
Give code examples
```

You can also include useful links, like this one with information about [formatting markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

You can 
- Also
- Make
- Lists

###############################################################################


DATA SET: A data frame with 189 observations measured on 11 variables.
    LINK: datarepository.wolframcloud.com/resources/Sample-Data-Birth-Weight-Risk
    Title: Birth Weight Risk
    Creator: D. W. Hosmer and S. Lemeshow
    Publisher: Wiley
    Date: 1989 #different than that stated in background
    Description: 9 potential risk factors for low birth weight with birth 
    weight outcomes.
BACKGROUND: This study focused on risks associated with low weight at birth; 
    the data were collected at the Baystate Medical Centre, Massachusetts, in 
    1986. Physicians have been interested in low weight at birth for several 
    years, because underweight babies have high rates of infant mortality and 
    infant anomalies. The behaviour of the mother-to-be during pregnancy (diet,
    smoking habits) can have a significant impact on the chances of having a 
    full-term pregnancy, and thus of giving birth to a child of normal weight. 
    The data file includes information on 189 women (identification number: ID) 
    who came to the centre for consultation. Weight at birth is categorized as 
    low if the child weighs less than 2,500 g.
    LINK: cran.r-project.org/web/packages/TRSbook/TRSbook.pdf 
    
    

PARSING: creates numpy arrays for each of the following variables
    ID: Identification
    LOW: Weight at birth less than 2,500g (false = 0, true = 1) - categorical outcome
    BWT: Birth weight, grams - numerical outcome
    AGE: Age of mother, years - numerical risk factor
    LWT: Weight of mother at last menstrual period, pounds - numerical risk factor
    PTL: Number of premature births in medical history - numerical risk factor
    FTV: Number of medical consultations during first trimester - numerical risk factor
    RACE: Race of mother (1=white, 2=black, 3=other) - categorical risk factor
    SMOKER: Smoking during pregnancy (false = 0, true = 1) - categorical risk factor
    HYPERTENSION: Medical history of hypertension (false = 0, true = 1) - categorical risk factor
    UI: Uterine irritability (false = 0, true = 1) - categorical risk factor

    
    
Individual Correlation
    Create function to compare BWT 
        to Age, LWT, Race, Smoker, PLT, Hypertension, UI, and FVT
    Analyze which have greatest impact
    Graph results with linear regression
    Graph correlation with descriptive statistics 
        (distribution, confidence intervals)

Mulitdimensional Clustering
    compare to classification (Low)
