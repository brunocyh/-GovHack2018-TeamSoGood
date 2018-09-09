# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:40:07 2017

@author: Bruno
"""
from sklearn.ensemble import RandomForestClassifier
from collections import OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# pima-indians-diabetes.csv

def featureImportance(df_X, df_y, filtered=10):
    """
    Input: 
        - features as dataframe
        - labels as dataframe
        
    Output: 
        - graph (just to document them)
    """
    # Run ensembled Tree algorithms, get importance (info gain) for each features
    rnd_clf = RandomForestClassifier(n_estimators=500)
    rnd_clf.fit(df_X, df_y)
    importances = dict()
    
    # Quantifying features importance (display)    
    for i, im in zip(df_X, rnd_clf.feature_importances_):
        importances.update({i:im})
    
    # Sort dict && listing
    importances = OrderedDict(sorted(importances.items(), key=lambda item: item[1], reverse=True))    
    f = [i for i in importances]
    v = [i for i in importances.values()]
    
    # filtered the first k results
    f = f[0:filtered]
    v = v[0:filtered]
    
    # Extracting importance from random forest internal 
    plt.title('Feature Importances')
    plt.barh(range(len(f)), v, color='b', align='center')
    plt.yticks(range(len(f)), f)
    plt.xlabel('Relative Importance')
    return plt
    