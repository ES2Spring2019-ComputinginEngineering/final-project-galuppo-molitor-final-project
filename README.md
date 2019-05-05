# Analysis and Visualization of Birthweight Data

The objective of this project was to create a tool for visualizing and analyzing a complex, large, and multidimensional dataset to make it more understandable.

The dataset we chose to demonstate this on considers the factors that may propose risk on birth weight. This particular dataset was strong in that it had a large number of datapoints (~200) and considered various different associated variables observable in a pregnant mothers that can be compared statistically.

These variables included:
- Mother’s age
- Pre-pregnancy body weight
- Smoker status during pregnancy
- History of hypertension
- Uterine irritability
- Race
- History of premature births
- Number of medical consultations during the first trimester

The Outcome:
- Birth weight of child in grams (classified as either normal or low)


## Instructions

This code was designed to be easily understood by the user. The "main.py" file includes all the necessary processing and outputs information that should
be useful to the user. In running the main file, all the necessary functions will be called and run accordingly resulting in formatted graphs, statistics,
and summary of results on this dataset - no further user interaction is necessary.

### Understanding The Output:
- formatting: titles and division lines for organization
- graphs: scatter plots (only for continuous data) and density curves
- statistics: descriptive stats formatted into tables and significance testing with explanations
- summary of results: shows all significance and comparative effect table for those variables found to be significant in both tests

*Note: header-lines and tables are best viewed at a particular console width that allows for the entire bar to be shown in a single line.*

## File List

### DataParsing.py
This file parses through the imported csv file and formats it into usable lists and arrays that are used in future functions.

*Libraries: Numpy, Matplotlib, Seaborn*

### Functions.py
This file creates all the necessary functions for graphing of data, statistical analysis, significance testing, summarizing of results, and formatting of outputs.

*Libraries: Numpy, Matplotlib, Scipy, Astropy, Statistics*

### Main.py
This file is the driver, which takes in and runs all the functions from each of the other files with the correct parameters and in the correct order. 
This will output the formatted user-oriented results that visualize and analyze the dataset.

