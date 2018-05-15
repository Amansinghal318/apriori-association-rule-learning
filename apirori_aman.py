# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:42:31 2018

@author: dell 1
"""

#apriori
#import the library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import the dataset
dataset=pd.read_csv('Market_Basket_Optimisation.csv',header=None)
transaction=[]
for i in range(0,7501):
 transaction.append([str(dataset.values[i,j])for j in range(0,20)])
#training apriori on dataset
 from apyori import apriori
 rules=apriori(transaction,min_support=0.03,min_confidence=0.2,min_lift=3,min_lenght=2)
 #visualizing the result
 result1=list(rules)
    