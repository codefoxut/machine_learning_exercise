#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:33:52 2018

@author: ujjwal
"""
# simple Linear Regression

# importing the libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the Dataset
dataset = pd.read_csv('data/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
 