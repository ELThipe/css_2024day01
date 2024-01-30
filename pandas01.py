# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:05:25 2024

@author: elthipe
"""

import pandas
file=pandas.read_csv("country_data.csv")
print (file)
print(file.info())
print(file.describe())

print("file1")
file2=pandas.read_csv("iris.csv")
print(file2)
print(file2.info())
print(file2.describe())

print("file2")
file=pandas.read_csv("housing_data.csv")
print(file)
print(file.info())
print(file.describe())

file3=pandas.read_csv('insurance_data.csv',skiprows=7)
print(file3)
print(file3.info())
print(file3.describe())
