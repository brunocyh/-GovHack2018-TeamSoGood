# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 20:55:24 2018

@author: BrunoAdmin
"""

import pandas as pd
import numpy as np

# Read postcode map
f_name = 'mod_postcode_suburb_mapping.csv'
df_suburb = pd.read_csv(f_name)
np_pc = df_suburb['postcode'].values

# covert suburb to postcode
map_set = {}
for indx, i in enumerate(df_suburb['suburb'].values):
    map_set.update({i: np_pc[indx]})


f_name = 'customer_waiting_time.csv'
df_wait = pd.read_csv(f_name)
df_wait['Service Location Name'] = df_wait['Service Location Name'].str.lower()

ll = []
array = []


def _find_suburb_for_this_servicecentre(service_centre, suburb_list):
    
    for suburb in suburb_list:
        if suburb in service_centre:
            return suburb_list.get(suburb)
        
    #print(service_centre)
    return 0

for index, suburb_centre in enumerate(df_wait['Service Location Name']):    
    pc = _find_suburb_for_this_servicecentre(suburb_centre, map_set)
    array.append(pc)
        
df_wait['Postcode'] = array
df_wait.to_csv('mod_customer_waiting_time.csv', index=False)

# Groupby
df_last = df_wait.groupby(['Postcode'])['Postcode','Average Wait Seconds','Average Serve Seconds', 'Number of Customers'].mean()
df_last.to_csv('last_customer_waiting_time.csv', index=False)
