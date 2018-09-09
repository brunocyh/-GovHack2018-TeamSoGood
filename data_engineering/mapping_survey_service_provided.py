# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 17:28:54 2018

@author: BrunoAdmin
"""

import chardet
import pandas as pd
import re
import numpy as np

from enum import Enum
from mapping_class import Mapper

f_name = 'service_centre.csv'

with open(f_name, 'rb') as f:
    result = chardet.detect(f.read())  # or readline if the file is large


df = pd.read_csv(f_name, encoding=result['encoding'])
service_provided = df[['Keywords','Postcode']]
service_provided = service_provided.sort_values(by=['Postcode']).reset_index(drop=True)

    
# Postcode, Category service one hot encode
new_ls = []
column = ['Postcode', 'Car and Motorbike related Service', 'Fine payment and Lawsuit', 'Business Service',
           'General Information Service', 'Personal, Permit and Other Services', 'Public transport',
           'Driving Test', 'Boat related Service']
columns_map = {'Car and Motorbike related Service':0, 'Fine payment and Lawsuit':1, 'Business Service':2,
               'General Information Service':3, 'Personal, Permit and Other Services':4, 'Public transport':5,
               'Driving Test':6, 'Boat related Service':7}
mapper = Mapper()

prev_pc = -1
prev_row = [0,0,0,0,0,0,0,0,0]

for row_num, row_list in enumerate(service_provided['Keywords']):
    # additional info
    pc = service_provided['Postcode'][row_num]
    row = [pc, 0,0,0,0,0,0,0,0]
    
    if pc == prev_pc:
        if type(row_list) == str:
            row_splited = re.split(';|,', row_list)
            
            for key_word in row_splited:
                key_word = key_word.strip(" ")
                key_word = mapper.convert(key_word)
                
                try: 
                    index = columns_map.get(key_word) + 1
                    row[index] = 1
                    
                except:
                    pass
                
            # this row compare with previous row
            a = np.array(prev_row[1:])
            b = np.array(row[1:])
            n = a + b
            
            new_row = [pc]
            new_row.extend(n)
            
            # modify the top row
            new_ls[-1] = new_row
                
        else:
            pass
    
    else:
        if type(row_list) == str:
            row_splited = re.split(';|,', row_list)
            
            for key_word in row_splited:
                key_word = key_word.strip(" ")
                key_word = mapper.convert(key_word)
                
                try: 
                    index = columns_map.get(key_word) + 1
                    row[index] = 1
                    
                except:
                    pass
                
        else:
            pass
    
        # apend this row
        new_ls.append(row)
        
    # End this row
    prev_pc = pc
    prev_row = row
    
new_data = pd.DataFrame(np.array(new_ls), columns = column)

# Apply 1 to >1
new_data=new_data.replace(to_replace=[2,3,4,5,6],value=1)
new_data.to_csv('postcode&serviceprovided.csv', index=False)