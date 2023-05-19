"""
Version 6 (Final Vesrsion) of strings document/program:

- Includes all new options in a large string
"""

import sys

options = """
Enter corresponding number for your choice (Type 'q' to return to the main menu):
1) Calculate the mean value of a specified substance/column's data
2) Calculate the minimum, maximum and range of a specified substance/column's data
3) Calculate the modes for a specified substance/column's data
4) Calculate the quartiles (Q1, Q2 (median) and Q3) as well as IQR of a specified substance/column's data
5) Calculate the variance and standard deviation of a specified substance/column's data
6) Get a summary of a certain substance/column's data (includes all calculations from options 1 - 4) 
and write this summary to a text file for later use
7) Calulcate the z-score for a certain value in a specified substance/column's data
8) Check for outliers in all substances/column's data and return which values are outliers 
and how many outliers there are
9) Remove all outliers from each column's data and make new sheet with alterations, 
then fill in all blank cells with either a) mean or b) median and copy alterations to new sheet
10) Graph data from a specified substance/column in a line graph
11) Graph data from a specified substance/column for a certain range in a line graph
12) Determine which data values for a specified substance/column are outside a specified range
"""