# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:48:11 2017

@author: Bruno
"""

import pandas as pd
import numpy as np
import feature_selection as fs


for i in range(0, 5):
    # Input variables (most test/trails)
    df = pd.read_csv('x.csv')
    
    # Indepent variables
    df_x = df.iloc[:,[0,1,3,4,5]]
    #df_x.info()
    
    
    # dependent variables
    df_y = pd.read_csv('y.csv')
    df_y = df_y.iloc[:,[i]]
    df_y = df_y.fillna(10)
    #df_y.info()
    
    # plot importances
    plt = fs.featureImportance(df_x, df_y, 5)
    print('Showing feature importance...')
    plt.show()