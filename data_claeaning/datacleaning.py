# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:07:12 2018

@author: BrunoAdmin
"""


import pandas as pd

# Input
df = pd.read_csv('raw_survey.csv')

# Fill empty
df.fillna("")

# Take away strings
df = df.drop(columns=['E1_15_TEXT', 'E3_TEXT', 'H7_5_TEXT', 'Z5_TEXT'])

# Replace values
df['B2b']=df['B2b'].replace(to_replace=99,value=int(6))
df['E7']=df['E7'].replace(to_replace=99,value="")
df['H1']=df['H1'].replace(to_replace=99,value="")
df['H8']=df['H8'].replace(to_replace=99,value=int(3)) # unsure -> 3
df['Z5']=df['Z5'].replace(to_replace=97,value=int(9))
df['SC4']=df['SC4'].replace(to_replace=[i for i in range(0,3999)],value="")



# SHow info
df.info()

# Output
df.to_csv('cleaned_survey.csv', index=False)

# Select columns
demo_satisfaction = ['SC2','SC3','SC4','B2b','H9New','H10','H11','H12','Z1','Z5','Z10','WEIGHT']
df[demo_satisfaction].to_csv('demo_satisfaction.csv', index=False)